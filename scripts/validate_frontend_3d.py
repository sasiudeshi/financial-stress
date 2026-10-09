"""Self-check for the 3D weather scene / results choreography enhancement.

Usage:
    python scripts/validate_frontend_3d.py
"""
import shutil
import subprocess
import sys
import time
from pathlib import Path

import pandas as pd
import requests
from fastapi.testclient import TestClient

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.validate_api import row_to_payload  # noqa: E402
from src.app.api import app  # noqa: E402

STATIC_DIR = REPO_ROOT / "src" / "app" / "static"
JS_PATH = STATIC_DIR / "app.js"
FIGURES_DIR = REPO_ROOT / "reports" / "figures"
CLEANED_PATH = REPO_ROOT / "data" / "processed" / "cleaned_data.csv"

LIVE_HOST = "127.0.0.1"
LIVE_PORT = 8931
LIVE_URL = f"http://{LIVE_HOST}:{LIVE_PORT}"

# Users confirmed (via a live /predict call) to actually be classified as
# Low / Moderate / High by the current model -- not just their historical
# true label, since predicted != true for some users (see model training
# stage notes on U100015).
SAMPLE_USERS = {"Low": "U100021", "Moderate": "U100000", "High": "U100004"}


def check(results, label, passed, reason=""):
    if passed:
        results.append(f"{label}: [PASS]")
    else:
        results.append(f"{label}: [FAIL]: {reason}")


def run_pytest(results):
    proc = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-q"],
                           cwd=str(REPO_ROOT), capture_output=True, text=True)
    output = proc.stdout + proc.stderr
    summary_line = ""
    for line in output.splitlines():
        if " passed" in line or " failed" in line or " error" in line:
            summary_line = line.strip()
    passed_ok = proc.returncode == 0 and "failed" not in summary_line and "error" not in summary_line
    check(results, f"Full pytest suite still passes ({summary_line or 'no summary parsed'})",
          passed_ok, output[-500:] if not passed_ok else "")
    print(f"pytest summary: {summary_line}")


def run_static_checks(results, client):
    resp = client.get("/")
    check(results, "GET / returns 200", resp.status_code == 200, f"status={resp.status_code}")

    node_path = shutil.which("node")
    if node_path is None:
        check(results, "node --check passes on app.js", False, "Node.js not found on PATH")
    else:
        proc = subprocess.run([node_path, "--check", str(JS_PATH)], capture_output=True, text=True)
        check(results, "node --check passes on app.js", proc.returncode == 0,
              proc.stderr.strip() or f"exit {proc.returncode}")


def wait_for_server(url, timeout=20):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(url + "/health", timeout=1)
            if r.status_code == 200:
                return True
        except requests.exceptions.RequestException:
            pass
        time.sleep(0.3)
    return False


def fill_and_submit(page, payload):
    for name, value in payload.items():
        selector = f'[name="{name}"]'
        tag = page.eval_on_selector(selector, "el => el.tagName.toLowerCase()")
        if tag == "select":
            page.select_option(selector, str(value))
        else:
            page.fill(selector, str(value))
    page.click("#submit-btn")
    page.wait_for_selector("#results-view:not([hidden])", timeout=10000)
    page.wait_for_function(
        'document.getElementById("results-visual").dataset.weatherReady === "true"', timeout=8000
    )
    # Wait for the FULL choreography to finish, not just the visual: the
    # confidence bars and cascading factor/recommendation cards reveal on
    # their own later staggered schedule (see runResultsChoreography in
    # app.js) -- a short fixed wait after weatherReady alone would still
    # catch the screenshot mid-sequence.
    page.wait_for_function(
        """() => {
          const confidence = document.querySelector('.confidence');
          const cascadeItems = document.querySelectorAll('.cascade-item');
          if (!confidence || !confidence.classList.contains('stage-visible')) return false;
          if (cascadeItems.length === 0) return false;
          return Array.from(cascadeItems).every(el => el.classList.contains('stage-visible'));
        }""",
        timeout=8000,
    )
    page.wait_for_timeout(300)  # let the last transition visually settle


def run_browser_checks(results):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        check(results, "3 per-state result screenshots saved", False, "Playwright not installed -- not silently skipped")
        check(results, "Reduced-motion fallback screenshot confirms static (non-3D) rendering", False,
              "Playwright not installed -- not silently skipped")
        check(results, "No JavaScript console errors during load -> fill -> submit -> results flow", False,
              "Playwright not installed -- not silently skipped")
        return

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    cleaned_df = pd.read_csv(CLEANED_PATH).set_index("user_id")

    server_proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "src.app.api:app", "--host", LIVE_HOST, "--port", str(LIVE_PORT)],
        cwd=str(REPO_ROOT), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        if not wait_for_server(LIVE_URL):
            check(results, "3 per-state result screenshots saved", False, "live server did not start")
            check(results, "Reduced-motion fallback screenshot confirms static (non-3D) rendering", False,
                  "live server did not start")
            check(results, "No JavaScript console errors during load -> fill -> submit -> results flow", False,
                  "live server did not start")
            return

        with sync_playwright() as p:
            browser = p.chromium.launch()

            # --- 3: one screenshot per state, using genuinely-predicted users ---
            screenshot_ok = True
            screenshot_reasons = []
            console_errors_all = []

            for level, uid in SAMPLE_USERS.items():
                payload = row_to_payload(cleaned_df.loc[uid])
                page = browser.new_page(viewport={"width": 900, "height": 1400})
                console_errors = []
                page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
                page.on("pageerror", lambda exc: console_errors.append(str(exc)))

                page.goto(LIVE_URL, wait_until="networkidle")
                fill_and_submit(page, payload)

                actual_level = page.get_attribute("#results-heading", "data-level")
                if actual_level != level:
                    screenshot_ok = False
                    screenshot_reasons.append(f"user {uid} expected to predict {level}, got {actual_level}")

                out_path = FIGURES_DIR / f"result_{level.lower()}.png"
                page.screenshot(path=str(out_path), full_page=True)

                canvas_present = page.eval_on_selector_all("#results-visual canvas", "els => els.length") == 1
                if not canvas_present:
                    screenshot_ok = False
                    screenshot_reasons.append(f"{level}: expected a 3D canvas, none found")

                console_errors_all.extend((level, e) for e in console_errors)
                page.close()

            check(
                results,
                "3 per-state result screenshots saved (result_low.png, result_moderate.png, result_high.png)",
                screenshot_ok,
                "; ".join(screenshot_reasons),
            )
            for level in SAMPLE_USERS:
                print(f"  saved {FIGURES_DIR / ('result_' + level.lower() + '.png')}")

            # --- 4: reduced-motion fallback ---
            page = browser.new_page(viewport={"width": 900, "height": 1400})
            page.emulate_media(reduced_motion="reduce")
            reduced_console_errors = []
            page.on("console", lambda msg: reduced_console_errors.append(msg.text) if msg.type == "error" else None)
            page.on("pageerror", lambda exc: reduced_console_errors.append(str(exc)))

            page.goto(LIVE_URL, wait_until="networkidle")
            reveal_opacities = page.eval_on_selector_all(
                ".reveal", "els => els.map(el => getComputedStyle(el).opacity)"
            )
            payload = row_to_payload(cleaned_df.loc[SAMPLE_USERS["High"]])
            fill_and_submit(page, payload)

            fallback_info = page.evaluate(
                """() => {
                  const container = document.getElementById('results-visual');
                  return {
                    canvasCount: container.querySelectorAll('canvas').length,
                    svgCount: container.querySelectorAll('svg').length,
                  };
                }"""
            )
            reduced_path = FIGURES_DIR / "result_reduced_motion.png"
            page.screenshot(path=str(reduced_path), full_page=True)
            page.close()

            reduced_ok = (
                all(op == "1" for op in reveal_opacities)
                and fallback_info["canvasCount"] == 0
                and fallback_info["svgCount"] == 1
            )
            check(
                results,
                "Reduced-motion fallback confirmed: form sections pre-visible, static SVG used (no 3D canvas)",
                reduced_ok,
                f"reveal_opacities={reveal_opacities}, fallback_info={fallback_info}",
            )
            print(f"  saved {reduced_path}")
            console_errors_all.extend(("reduced-motion", e) for e in reduced_console_errors)

            browser.close()

        check(
            results,
            "No JavaScript console errors during load -> fill -> submit -> results flow (any state)",
            not console_errors_all,
            f"errors: {console_errors_all}",
        )
    finally:
        server_proc.terminate()
        try:
            server_proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            server_proc.kill()


def main():
    results = []
    client = TestClient(app)

    run_pytest(results)
    run_static_checks(results, client)
    run_browser_checks(results)

    print()
    print("=== 3D Weather Scene / Choreography Self-Check ===")
    for line in results:
        print(line)

    all_passed = all("[FAIL]" not in r for r in results)
    print()
    print("OVERALL:", "ALL CHECKS PASSED" if all_passed else "ONE OR MORE CHECKS FAILED")
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
