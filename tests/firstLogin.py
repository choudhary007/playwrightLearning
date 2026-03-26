from playwright.sync_api import sync_playwright

def firstLogin():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        # page.wait_for_timeout(10000)
        page.locator("#username").fill("tomsmith")
        # page.locator("#password").fill("SuperSecretPassword!")
        page.locator("#password").fill("123edsffe!")
        page.click("button[type='submit']")
        # page.wait_for_timeout(5000)
        text = page.text_content("#flash")
        print(text)

if __name__ == "__main__":
    firstLogin()