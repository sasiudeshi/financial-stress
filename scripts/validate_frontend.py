"""Self-check the frontend (src/app/static/) and its integration with the API.

Usage:
    python scripts/validate_frontend.py
"""
import shutil
import subprocess
import sys
import time
from pathlib import Path

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

EXPECTED_PREDICT_FIELDS = {
    "financial_stress_level", "confidence", "contributing_factors", "recommendations", "disclaimer",
}

LIVE_HOST = "127.0.0.1"
LIVE_PORT = 8765
LIVE_URL = f"http://{LIVE_HOST}:{LIVE_PORT}"


def check(results, label, passed, reason=""):
    if passed:
        results.append(f"{label}: [PASS]")
    else:
        results.append(f"{label}: [FAIL]: {reason}")


def get_sample_payload():
    import pandas as pd
    cleaned_df = pd.read_csv(CLEANED_PATH).set_index("user_id")
    # Same sample user used throughout the model training / API stages (true High class).
    row = cleaned_df.loc["U100004"]
    return row_to_payload(row)


def run_static_checks(results, client):
    # 1. GET / -> 200, text/html
    resp = client.get("/")
    check(
        results,
        "GET / returns 200 with Content-Type text/html",
        resp.status_code == 200 and "text/html" in resp.headers.get("content-type", ""),
        f"status={resp.status_code}, content-type={resp.headers.get('content-type')}",
    )

    # 2. CSS and JS served with 200
    css_resp = client.get("/style.css")
    js_resp = client.get("/app.js")
    check(
        results,
        "style.css and app.js are served with 200 status",
        css_resp.status_code == 200 and js_resp.status_code == 200,
        f"style.css={css_resp.status_code}, app.js={js_resp.status_code}",
    )

    # 3. node --check on the JS file
    node_path = shutil.which("node")
    if node_path is None:
        check(results, "node --check confirms app.js has no syntax errors", False,
              "Node.js not found on PATH -- syntax check skipped, not silently passed")
    else:
        proc = subprocess.run([node_path, "--check", str(JS_PATH)], capture_output=True, text=True)
        check(
            results,
            "node --check confirms app.js has no syntax errors",
            proc.returncode == 0,
            proc.stderr.strip() or f"node --check exited with {proc.returncode}",
        )

    # 4. POST /predict with a real sample user, check expected response fields
    payload = get_sample_payload()
    predict_resp = client.post("/predict", json=payload)
    if predict_resp.status_code != 200:
        check(results, "POST /predict returns all expected fields for a valid sample user", False,
              f"status={predict_resp.status_code}: {predict_resp.text}")
    else:
        body = predict_resp.json()
        missing = EXPECTED_PREDICT_FIELDS - set(body.keys())
        check(
            results,
            "POST /predict returns all expected fields for a valid sample user",
            not missing,
            f"missing fields: {sorted(missing)}" if missing else "",
        )

    return payload


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


def run_playwright_checks(results, payload):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        check(results, "Playwright screenshots of loaded page and results view", False,
              "Playwright is not installed in this environment -- screenshots skipped, not silently passed")
        print("Playwright not available: cannot describe rendered output visually; skipping screenshots.")
        return

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    server_proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "src.app.api:app", "--host", LIVE_HOST, "--port", str(LIVE_PORT)],
        cwd=str(REPO_ROOT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        if not wait_for_server(LIVE_URL):
            check(results, "Playwright screenshots of loaded page and results view", False,
                  "Live uvicorn server did not become ready in time")
            return

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 900, "height": 1400})
            page.goto(LIVE_URL, wait_until="networkidle")

            # Viewport-only (not full_page): a full_page capture stitches
            # multiple viewport tiles, and Chromium bakes a position:sticky
            # element (the submit bar) into whatever mid-scroll position it
            # occupied during stitching, producing a floating artifact that
            # doesn't reflect real scrolling behavior. Viewport capture avoids it.
            loaded_path = FIGURES_DIR / "frontend_loaded.png"
            page.screenshot(path=str(loaded_path), full_page=False)

            for name, value in payload.items():
                selector = f'[name="{name}"]'
                tag = page.eval_on_selector(selector, "el => el.tagName.toLowerCase()")
                if tag == "select":
                    page.select_option(selector, str(value))
                else:
                    page.fill(selector, str(value))

            page.click("#submit-btn")
            page.wait_for_selector("#results-view:not([hidden])", timeout=10000)
            page.wait_for_timeout(700)  # let the results-in animation settle

            results_path = FIGURES_DIR / "frontend_results.png"
            page.screenshot(path=str(results_path), full_page=True)

            browser.close()

        check(
            results,
            "Playwright screenshots of loaded page and results view saved to reports/figures/",
            loaded_path.exists() and loaded_path.stat().st_size > 0
            and results_path.exists() and results_path.stat().st_size > 0,
            f"loaded_path exists={loaded_path.exists()}, results_path exists={results_path.exists()}",
        )
        print(f"Saved {loaded_path}")
        print(f"Saved {results_path}")
    finally:
        server_proc.terminate()
        try:
            server_proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            server_proc.kill()


def main():
    results = []
    client = TestClient(app)

    payload = run_static_checks(results, client)
    run_playwright_checks(results, payload)

    print("=== Frontend Self-Check ===")
    for line in results:
        print(line)

    all_passed = all("[FAIL]" not in r for r in results)
    print()
    print("OVERALL:", "ALL CHECKS PASSED" if all_passed else "ONE OR MORE CHECKS FAILED")
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
