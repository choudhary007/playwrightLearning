import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL_DROPDOWN = "https://the-internet.herokuapp.com/dropdown"
BASE_URL_CHECKBOX = "https://the-internet.herokuapp.com/checkboxes"
BASE_URL = "https://the-internet.herokuapp.com"

@pytest.fixture
def page():
      with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_dropdown(page):
    page.goto(BASE_URL_DROPDOWN)
    expect(page).to_have_url(BASE_URL_DROPDOWN)
    page.select_option("#dropdown", label="Option 1")
    expect(page.locator("#dropdown")).to_have_value("1")

def test_checkbox(page):
    page.goto(BASE_URL_CHECKBOX)
    expect(page).to_have_url(BASE_URL_CHECKBOX)
    checkboxe1 = page.locator("input[type=checkbox]").nth(0)
    checkboxe1.check()
    expect(checkboxe1).to_be_checked()
    checkboxe1.uncheck()
    expect(checkboxe1).not_to_be_checked()

def test_keyboard_login(page):
    page.goto(f"{BASE_URL}/login")
    expect(page).to_have_url(f"{BASE_URL}/login")
    page.fill("#username", "tomsmith")
    page.press("#username", "Tab")
    page.fill("#password", "SuperSecretPassword!")
    page.keyboard.press("Enter")
    expect(page).to_have_url(f"{BASE_URL}/secure")
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).not_to_be_visible()
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url(f"{BASE_URL}/login")
    expect(page.locator("#flash")).to_contain_text("You logged out of the secure area!")

