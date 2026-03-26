import os

import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://the-internet.herokuapp.com"

@pytest.fixture
def page():
      with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

def handle_prompt(dialog):
    dialog.accept("Hello")

@pytest.mark.smoke
def test_accept_alert(page):
    page.goto(f"{BASE_URL}/javascript_alerts")
    expect(page).to_have_url(f"{BASE_URL}/javascript_alerts")

    page.on("dialog", lambda dialog: dialog.accept())
    page.click("text=Click for JS Alert")
    expect(page.locator("#result")).to_contain_text("You successfully clicked an alert")

# def test_dismiss_alert(page):
#     page.goto(f"{BASE_URL}/javascript_alerts")
#     expect(page).to_have_url(f"{BASE_URL}/javascript_alerts")

#     page.on("dialog", lambda dialog: dialog.dismiss())
#     page.click("text=Click for JS Confirm")
#     expect(page.locator("#result")).to_contain_text("You clicked: Cancel")

# def test_prompt_alert(page):
#     page.goto(f"{BASE_URL}/javascript_alerts")
#     expect(page).to_have_url(f"{BASE_URL}/javascript_alerts")
#     page.on("dialog", handle_prompt)
#     page.click("text=Click for JS Prompt")
#     expect(page.locator("#result")).to_contain_text("You entered: Hello")

@pytest.mark.regression
def test_handle_iframe(page):
    page.goto("https://www.selenium.dev/selenium/web/iframes.html")

    # Step 1: wait for iframe
    iframe = page.locator("#iframe1")
    expect(iframe).to_be_visible()

    # Step 2: switch using frame_locator
    frame = page.frame_locator("#iframe1")

    # Step 3: wait for element inside iframe
    input_box = frame.locator("#email")
    expect(input_box).to_be_visible()

    # Step 4: interact
    input_box.fill("Hello Deepak Choudhary")

    # Step 5: validate
    expect(input_box).to_have_value("Hello Deepak Choudhary")

# def test_upload_file(page):
#     page.goto(f"{BASE_URL}/upload")
#     expect(page).to_have_url(f"{BASE_URL}/upload")
#     file_path = os.path.abspath("test_data/file_to_be_uploaded.txt")
#     page.set_input_files("#file-upload", file_path) 
#     page.click("#file-submit")
#     expect(page.locator("#uploaded-files")).to_contain_text("file_to_be_uploaded.txt")






