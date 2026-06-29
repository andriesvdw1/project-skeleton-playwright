from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from python_project.helper.utils import take_screenshot, log_message
from python_project.page_objects.base_page import BasePage
from python_project.page_objects.main_page import MainPage


class LoginPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)
        self.username_field = self.page.locator("[name = 'email']")
        self.password_field = self.page.locator("[name = 'pass']")
        self.login_button = self.page.locator( "[name = 'login']")

    def perform_login(self, username: str, password: str):
        log_message(self.logger, "performing login", level=logging.INFO)
        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)
        self.click_element(self.login_button)
        if self.login_button.is_visible():
            log_message(self.logger, "login failed", level=logging.ERROR)
            take_screenshot("login failed")
            return None
        return MainPage(self.page)
        # note MainPage class still needs to get written at this time




# perform, login
# log
# username
# password
# submit button
    # return main page
# fail - > log * screenshot
# fail test