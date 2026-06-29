import logging
from playwright.sync_api import Page
from python_project.helper.utils import take_screenshot, log_message, LogLevel
from python_project.page_objects.base_page import BasePage
from python_project.page_objects.main_page import MainPage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Cleaned up spacing in attributes for reliable matching
        self.username_field = self.page.locator("[name='email']")
        self.password_field = self.page.locator("[name='pass']")
        self.login_button = self.page.locator("[name='login']")

        # Cookie banner targets (Facebook displays these dynamically in clean test sessions)
        self.cookie_allow_buttons = self.page.locator(
            "button:has-text('Allow all cookies'), button:has-text('Only allow essential cookies'), button[data-testid*='accept']"
        )

    def perform_login(self, username: str, password: str):
        # 1. Clear cookie consent barriers if they obscure the screen
        try:
            if self.cookie_allow_buttons.first.is_visible(timeout=3000):
                log_message(self.logger, "Cookie overlay detected, dismissing...", level=LogLevel.INFO)
                self.cookie_allow_buttons.first.click()
        except Exception:
            # Bypass if no banner shows up
            pass

        # 2. Complete login operations
        log_message(self.logger, "Performing login sequence", level=LogLevel.INFO)
        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)
        self.click_element(self.login_button)

        # 3. Validation checkpoint
        # Give the transition a moment to process before judging success
        self.page.wait_for_timeout(1000)
        if self.login_button.is_visible():
            log_message(self.logger, "Login failed - fields are still visible", level=LogLevel.ERROR)
            # Fixed: Passed self.page reference into your project utility signature
            take_screenshot(self.page, "login_failed")
            return None

        return MainPage(self.page)