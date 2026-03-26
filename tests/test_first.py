from playwright.sync_api import sync_playwright

def test_open_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page1 = browser.new_page()
        # page.goto("https://www.google.com")
        page1.goto("https://demoqa.com")
        print(page1.title())   # just to verify

        browser.close()

if __name__ == "__main__":
    test_open_google()