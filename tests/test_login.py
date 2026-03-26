import pytest
from playwright.sync_api import expect, sync_playwright

BASE_URL = "https://the-internet.herokuapp.com"

def login(page, username, password):
    page.fill("#username", username)
    page.fill("#password", password)
    page.click("button[type='submit']")

@pytest.fixture
def page():
      with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_valid_login(page):
        page.goto(f"{BASE_URL}/login")
        expect(page).to_have_url(f"{BASE_URL}/login")
        expect(page).to_have_title("The Internet")
        expect(page.locator("#username")).to_be_visible()
        expect(page.locator("#password")).to_be_visible()
        expect(page.locator("button[type='submit']")).to_be_visible()
        login(page, "tomsmith", "SuperSecretPassword!")
        expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")

def test_logout(page):
        page.goto(f"{BASE_URL}/login")
        expect(page).to_have_url(f"{BASE_URL}/login")
        login(page, "tomsmith", "SuperSecretPassword!")
        expect(page).to_have_url(f"{BASE_URL}/secure")
        expect(page).to_have_title("The Internet")
        expect(page.get_by_role("link", name="Logout")).to_be_visible()
        expect(page.get_by_role("button", name="submit")).not_to_be_visible()
        page.get_by_role("link", name="Logout").click()
        expect(page).to_have_url(f"{BASE_URL}/login")
        expect(page.locator("#flash")).to_contain_text("You logged out of the secure area!")

def test_invalid_pswd_login(page):
            page.goto(f"{BASE_URL}/login")
            expect(page).to_have_url(f"{BASE_URL}/login")
            login(page, "tomsmith", "SuperSecretPassword!123")
            expect(page.locator("#flash")).to_contain_text("Your password is invalid!")

def test_invalid_usr_login(page):
            page.goto(f"{BASE_URL}/login")
            expect(page).to_have_url(f"{BASE_URL}/login")
            login(page, "Deepak", "SuperSecretPassword!123")
            expect(page.locator("#flash")).to_contain_text("Your username is invalid!")
            page.reload()
            expect (page.locator("#flash")).not_to_be_visible()
