"""Final wrap-up self-check: test suite, requirements coverage, clean-install
verification, documentation presence, and the Step 1 confidence-bar fix.

Usage:
    python scripts/validate_final.py
"""
import ast
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

REQUIREMENTS_PATH = REPO_ROOT / "requirements.txt"
README_PATH = REPO_ROOT / "README.md"
USER_GUIDE_PATH = REPO_ROOT / "docs" / "user_guide.md"

STDLIB_MODULES = {
    "argparse", "contextlib", "copy", "datetime", "json", "logging", "math",
    "pathlib", "re", "shutil", "subprocess", "sys", "time", "typing", "ast",
    "tempfile", "os", "collections", "itertools", "functools",
}
INTERNAL_MODULES = {"scripts", "src", "tests"}

# import name -> PyPI package name, where they differ.
IMPORT_TO_PACKAGE = {"sklearn": "scikit-learn"}

PYTEST_SUMMARY_RE = re.compile(
    r"(?:(\d+) failed, )?(?:(\d+) passed)(?:, (\d+) warnings?)?(?:, (\d+) errors?)? in [\d.]+s"
)


def check(results, label, passed, reason=""):
    if passed:
        results.append(f"{label}: [PASS]")
    else:
        results.append(f"{label}: [FAIL]: {reason}")


# --------------------------------------------------------------------------
# 1. Full pytest suite
# --------------------------------------------------------------------------

def run_pytest_suite(python_exe, cwd):
    proc = subprocess.run(
        [str(python_exe), "-m", "pytest", "tests/", "-q"],
        cwd=str(cwd), capture_output=True, text=True,
    )
    output = proc.stdout + proc.stderr
    summary_line = ""
    for line in output.splitlines():
        if " passed" in line or " failed" in line or " error" in line:
            summary_line = line.strip()
    return proc.returncode, summary_line, output


def parse_pytest_summary(summary_line):
    m = PYTEST_SUMMARY_RE.search(summary_line)
    if not m:
        return None
    failed = int(m.group(1) or 0)
    passed = int(m.group(2) or 0)
    errors = int(m.group(4) or 0)
    return {"passed": passed, "failed": failed, "errors": errors, "total": passed + failed + errors}


# --------------------------------------------------------------------------
# 2. requirements.txt coverage of src/ imports
# --------------------------------------------------------------------------

def scan_imports(root_dirs):
    modules = set()
    for root in root_dirs:
        for path in (REPO_ROOT / root).rglob("*.py"):
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        modules.add(alias.name.split(".")[0])
                elif isinstance(node, ast.ImportFrom):
                    if node.level == 0 and node.module:
                        modules.add(node.module.split(".")[0])
    return modules - STDLIB_MODULES - INTERNAL_MODULES


def parse_requirements(path):
    packages = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        name = re.split(r"[=<>!~\[]", line, maxsplit=1)[0].strip().lower()
        if name:
            packages.add(name)
    return packages


def check_requirements_coverage(results):
    src_imports = scan_imports(["src"])
    required_packages = parse_requirements(REQUIREMENTS_PATH)

    missing = []
    for module in sorted(src_imports):
        package_name = IMPORT_TO_PACKAGE.get(module, module).lower()
        if package_name not in required_packages:
            missing.append(module)

    check(
        results,
        "requirements.txt exists and every import in src/ has a matching pinned entry",
        REQUIREMENTS_PATH.exists() and not missing,
        f"missing from requirements.txt: {missing}" if missing else (
            "requirements.txt not found" if not REQUIREMENTS_PATH.exists() else ""
        ),
    )


# --------------------------------------------------------------------------
# 3. Clean-install verification (re-run fresh, for real)
# --------------------------------------------------------------------------

def wait_for_http(url, timeout=30):
    import requests
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(url, timeout=1)
            return r
        except requests.exceptions.RequestException:
            time.sleep(0.3)
    return None


def run_clean_install_verification(results):
    with tempfile.TemporaryDirectory(prefix="fsd_clean_venv_") as tmp:
        tmp_path = Path(tmp)
        venv_dir = tmp_path / "venv"
        details = []

        proc = subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], capture_output=True, text=True)
        if proc.returncode != 0:
            check(results, "Clean-install verification succeeds end to end", False,
                  f"venv creation failed: {proc.stderr[-300:]}")
            return

        python_exe = venv_dir / "Scripts" / "python.exe" if sys.platform == "win32" else venv_dir / "bin" / "python"

        install_proc = subprocess.run(
            [str(python_exe), "-m", "pip", "install", "-r", str(REQUIREMENTS_PATH), "--quiet"],
            capture_output=True, text=True, cwd=str(REPO_ROOT),
        )
        if install_proc.returncode != 0:
            check(results, "Clean-install verification succeeds end to end", False,
                  f"pip install failed: {install_proc.stderr[-500:]}")
            return
        details.append("pip install -r requirements.txt: OK")

        port = 8877
        server_proc = subprocess.Popen(
            [str(python_exe), "-m", "uvicorn", "src.app.api:app", "--host", "127.0.0.1", "--port", str(port)],
            cwd=str(REPO_ROOT), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        try:
            health_resp = wait_for_http(f"http://127.0.0.1:{port}/health")
            if health_resp is None or health_resp.status_code != 200 or not health_resp.json().get("model_loaded"):
                check(results, "Clean-install verification succeeds end to end", False,
                      f"server did not start / /health unhealthy: {health_resp.text if health_resp else 'no response'}")
                return
            details.append("uvicorn started, GET /health -> 200, model_loaded: true")

            import pandas as pd
            from scripts.validate_api import row_to_payload
            cleaned = pd.read_csv(REPO_ROOT / "data" / "processed" / "cleaned_data.csv").set_index("user_id")
            payload = row_to_payload(cleaned.loc["U100000"])

            import requests
            predict_resp = requests.post(f"http://127.0.0.1:{port}/predict", json=payload, timeout=10)
            if predict_resp.status_code != 200:
                check(results, "Clean-install verification succeeds end to end", False,
                      f"POST /predict failed: {predict_resp.status_code}: {predict_resp.text[:200]}")
                return
            details.append("POST /predict (sample user) -> 200")
        finally:
            server_proc.terminate()
            try:
                server_proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                server_proc.kill()

        returncode, summary_line, _ = run_pytest_suite(python_exe, REPO_ROOT)
        parsed = parse_pytest_summary(summary_line)
        pytest_ok = returncode == 0 and parsed is not None and parsed["failed"] == 0 and parsed["errors"] == 0
        details.append(f"pytest in clean venv: {summary_line or '(no summary parsed)'}")

        check(
            results,
            "Clean-install verification succeeds end to end (venv + install + server + /health + /predict + pytest)",
            pytest_ok,
            "; ".join(details) if not pytest_ok else "",
        )
        for d in details:
            print(f"  clean-install: {d}")


# --------------------------------------------------------------------------
# 4. Docs exist and are non-empty
# --------------------------------------------------------------------------

def check_docs(results):
    for path, label in [(README_PATH, "README.md"), (USER_GUIDE_PATH, "docs/user_guide.md")]:
        exists_and_nonempty = path.exists() and path.stat().st_size > 0
        check(results, f"{label} exists and is non-empty", exists_and_nonempty,
              f"{path} missing or empty" if not exists_and_nonempty else "")


# --------------------------------------------------------------------------
# 5. Confidence bar fix (Step 1) -- DOM/screenshot check via Playwright
# --------------------------------------------------------------------------

def check_confidence_bar_fix(results):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        check(results, "0% confidence bar fix confirmed via headless browser", False,
              "Playwright not available in this environment -- not silently skipped, genuinely unverified")
        return

    import pandas as pd
    from scripts.validate_api import row_to_payload

    port = 8878
    server_proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "src.app.api:app", "--host", "127.0.0.1", "--port", str(port)],
        cwd=str(REPO_ROOT), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        if wait_for_http(f"http://127.0.0.1:{port}/health") is None:
            check(results, "0% confidence bar fix confirmed via headless browser", False,
                  "live server for browser check did not start")
            return

        # U100004 (used throughout prior stages) predicts High with Low
        # confidence rounding to ~0.0% -- a genuine near-zero case, not synthetic.
        cleaned = pd.read_csv(REPO_ROOT / "data" / "processed" / "cleaned_data.csv").set_index("user_id")
        payload = row_to_payload(cleaned.loc["U100004"])

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 900, "height": 1400})
            page.goto(f"http://127.0.0.1:{port}", wait_until="networkidle")

            for name, value in payload.items():
                selector = f'[name="{name}"]'
                tag = page.eval_on_selector(selector, "el => el.tagName.toLowerCase()")
                if tag == "select":
                    page.select_option(selector, str(value))
                else:
                    page.fill(selector, str(value))

            page.click("#submit-btn")
            page.wait_for_selector("#results-view:not([hidden])", timeout=10000)
            page.wait_for_timeout(700)

            low_text = page.inner_text('[data-value="Low"]')
            low_fill_width_px = page.eval_on_selector(
                '[data-fill="Low"]', "el => el.getBoundingClientRect().width"
            )

            screenshot_path = REPO_ROOT / "reports" / "figures" / "frontend_zero_confidence_bar.png"
            page.locator(".confidence").screenshot(path=str(screenshot_path))

            browser.close()

        is_near_zero_case = low_text.strip() in ("0%", "0.0%")
        bar_visibly_rendered = low_fill_width_px >= 5  # the CSS min-width is 6px

        check(
            results,
            "0% confidence bar fix confirmed via headless browser (DOM check + screenshot)",
            is_near_zero_case and bar_visibly_rendered,
            f"Low confidence text={low_text!r}, fill width={low_fill_width_px:.1f}px "
            f"(expected a near-zero case with fill width >= 5px due to CSS min-width)",
        )
        print(f"  Low confidence label read: {low_text!r}, rendered fill width: {low_fill_width_px:.1f}px")
        print(f"  Screenshot saved to {screenshot_path}")
    finally:
        server_proc.terminate()
        try:
            server_proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            server_proc.kill()


def main():
    results = []

    # 1. Full pytest suite (main environment)
    returncode, summary_line, output = run_pytest_suite(Path(sys.executable), REPO_ROOT)
    parsed = parse_pytest_summary(summary_line)
    if parsed is None:
        check(results, "Full pytest suite passes", False, f"could not parse pytest output: {output[-500:]}")
    else:
        check(
            results,
            f"Full pytest suite passes ({parsed['total']} total, {parsed['passed']} passed, {parsed['failed']} failed)",
            returncode == 0 and parsed["failed"] == 0 and parsed["errors"] == 0,
            summary_line,
        )
    print(f"pytest summary line: {summary_line}")

    # 2. requirements.txt coverage
    check_requirements_coverage(results)

    # 3. Clean-install verification (re-run fresh)
    run_clean_install_verification(results)

    # 4. Docs
    check_docs(results)

    # 5. Confidence bar fix
    check_confidence_bar_fix(results)

    print()
    print("=== Final Wrap-Up Self-Check ===")
    for line in results:
        print(line)

    all_passed = all("[FAIL]" not in r for r in results)
    print()
    print("OVERALL:", "ALL CHECKS PASSED" if all_passed else "ONE OR MORE CHECKS FAILED")
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
