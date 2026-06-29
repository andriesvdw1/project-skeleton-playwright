import logging

from playwright.async_api import expect
from playwright.sync_api import Page
from python_project.helper.utils import take_screenshot, log_message, LogLevel
from python_project.page_objects.base_page import BasePage
from python_project.page_objects.main_page import MainPage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_field = self.page.locator("[name='username']")
        self.password_field = self.page.locator("[name='password']")

        # Combined selector: Handles standard [name='login'] AND fallback button types
        self.login_button = self.page.locator(
            "[name='login'], button[type='submit'], [data-testid='royal_login_button']")

        self.cookie_allow_buttons = self.page.locator(
            "button:has-text('Allow all cookies'), button:has-text('Only allow essential cookies'), button[data-testid*='accept']"
        )

    def perform_login(self, username: str, password: str):
        # 1. Force Playwright to wait until the core form structure is visible
        log_message(self.logger, "Waiting for login screen initialization...", level=LogLevel.INFO)
        try:
            self.username_field.wait_for(state="visible", timeout=10000)
        except Exception:
            log_message(self.logger, "Form initialization timed out. Checking for overlays.", level=LogLevel.WARNING)

        # 2. Clear cookie consent barriers if they obscure the screen
        try:
            if self.cookie_allow_buttons.first.is_visible(timeout=2000):
                log_message(self.logger, "Cookie overlay detected, dismissing...", level=LogLevel.INFO)
                self.cookie_allow_buttons.first.click()
        except Exception:
            pass

        # 3. Complete login operations
        log_message(self.logger, "Performing login sequence", level=LogLevel.INFO)
        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)

        # Ensure the login button is attached and interactable before clicking
        self.login_button.first.wait_for(state="visible", timeout=5000)
        self.click_element(self.login_button.first)

        # 4. Validation checkpoint for your Invalid Credentials state
        self.page.wait_for_timeout(2000)
        if self.login_button.first.is_visible():
            log_message(self.logger, "Login failed - fields are still visible (Expected for invalid credentials)",
                        level=LogLevel.INFO)
            take_screenshot(self.page, "login_failed_expected")
            return None

        return MainPage(self.page)

    def verify_login(self):
        expect(self.login_button).to_be_visible(), "Failed to login"