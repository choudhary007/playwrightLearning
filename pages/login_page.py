from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_btn = page.get_by_role("button", name="Login")
        self.logout_btn = page.get_by_role("link", name="Logout")
        self.flash_msg = page.locator("#flash")

    def navigate(self, base_url):
        self.page.goto(f"{base_url}/login")

    def login(self, username, password):
        self.logger.info(f"Logging in with user: {username}")
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_btn)

    def logout(self):
        self.click(self.logout_btn)

    def is_logout_btn_visible(self):
        return self.logout_btn

    def get_flash_message(self):
        return self.flash_msg