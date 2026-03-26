from playwright.sync_api import expect, sync_playwright

def assertLogin():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        expect(page).to_have_url("https://the-internet.herokuapp.com/login")
        expect(page).to_have_title("The Internet")
        expect(page.locator("#username")).to_be_visible()
        expect(page.locator("#password")).to_be_visible()
        expect(page.locator("button[type='submit']")).to_be_visible()


        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        page.locator("button[type='submit']").click()
        expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
        expect(page).to_have_title("The Internet")
        expect(page.get_by_role("link", name="Logout")).to_be_visible()
        expect(page.locator("button[type='submit']")).not_to_be_visible()
        # expect(page.locator("h4")).to_contain_text("Welcome to the Secure Area. When you are done click logout below.")

        page.get_by_role("link", name="Logout").click()
        expect(page).to_have_url("https://the-internet.herokuapp.com/login")
        expect(page.locator("#flash")).to_contain_text("You logged out of the secure area!")

        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!123")
        page.locator("button[type='submit']").click()
        expect(page.locator("#flash")).to_contain_text("Your password is invalid!")

        page.locator("#username").fill("Deepak")
        page.locator("#password").fill("SuperSecretPassword!")
        page.locator("button[type='submit']").click()
        expect(page.locator("#flash")).to_contain_text("Your username is invalid!")

        page.reload()
        expect (page.locator("#flash")).not_to_be_visible()

        browser.close()

if __name__ =="__main__":
    assertLogin()
