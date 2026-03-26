import pytest
import os
from playwright.sync_api import sync_playwright
from datetime import datetime

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "Playwright Framework"
        config._metadata["Tester"] = "Deepak"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when in ["setup", "call"] and report.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.nodeid.replace("::", "_").replace("/", "_")

            screenshot_path = f"screenshots/{test_name}_{timestamp}.png"

            page.screenshot(path=screenshot_path)

            print(f"Screenshot saved at: {screenshot_path}")