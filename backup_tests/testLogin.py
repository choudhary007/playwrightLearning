from playwright.sync_api import expect, sync_playwright

def testLogin ():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com/")
        search_box = page.locator("textarea[name='q']")
        expect(search_box).to_be_visible()
        search_box.fill("Playwright pyhton")

        search_box.press("Enter")
        # page.wait_for_load_state("load")
        # expect(page).to_have_title(lambda title: "Playwright" in title)
        expect(page.locator("h3")).to_be_visible()
        print(page.title())
        browser.close()

if __name__ == "__main__":
    testLogin()
