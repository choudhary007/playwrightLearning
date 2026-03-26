import pytest
from utils.data_loader import load_test_data
from pages.login_page import LoginPage
from utils.config import BASE_URL
from playwright.sync_api import expect
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "test_data", "login_data.json")
test_data = load_test_data(file_path)

@pytest.mark.parametrize("data", test_data)

# @pytest.mark.parametrize("username, password, expected_msg", [("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
#                                                               ("Deepak", "SuperSecretPassword!", "Your username is invalid!"),])

# BASE_URL = "https://the-internet.herokuapp.com"




def test_login_scenarios(page, data):
    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login(data["username"], data["password"])
    expect(login_page.get_flash_message()).to_contain_text(data["expected"])


# def test_valid_login_logout(page):
#         login_page = LoginPage(page)

#         login_page.navigate(BASE_URL)
#         login_page.login(USERNAME, PASSWORD)
#         expect(page).to_have_url(f"{BASE_URL}/secure")
#         expect(login_page.get_flash_message()).to_contain_text("You logged into a secure area!")
#         expect(login_page.is_logout_btn_visible()).to_be_visible()
#         login_page.logout()
#         expect(login_page.get_flash_message()).to_contain_text("You logged out of the secure area!")
#         expect(page).to_have_url(f"{BASE_URL}/login")

# def test_invalid_pswd_login(page):
#             login_page = LoginPage(page)

#             login_page.navigate(BASE_URL)
#             expect(page).to_have_url(f"{BASE_URL}/login")
#             login_page.login("tomsmith", "SuperSecretPassword!123")
#             expect(login_page.get_flash_message()).to_contain_text("Your password is invalid!")

# def test_invalid_usr_login(page):
#             login_page = LoginPage(page)

#             login_page.navigate(BASE_URL)
#             expect(page).to_have_url(f"{BASE_URL}/login")
#             login_page.login("Deepak", "SuperSecretPassword!123")
#             expect(login_page.get_flash_message()).to_contain_text("Your username is invalid!")
#             page.reload()
#             expect (login_page.get_flash_message()).not_to_be_visible()
