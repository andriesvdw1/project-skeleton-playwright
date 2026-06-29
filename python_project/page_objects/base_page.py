import logging
from playwright.sync_api import Page, Locator
from python_project.helper.utils import LogLevel, take_screenshot, log_message


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        # Creates a unique logger named after the specific Page Object class
        self.logger = logging.getLogger(self.__class__.__name__)

    def safe_execute(self, action, name, *args, **kwargs):
        try:
            # Fixed: Changed 'action_name' to 'name' to match the parameter
            log_message(self.logger, f"Executing {name} with arguments {args}", LogLevel.INFO)

            # Fixed: Added **kwargs so Playwright parameters are sent correctly
            # Fixed: Added 'return' so functions can return elements or text values
            return action(*args, **kwargs)
        except Exception as e:
            log_message(self.logger, f"Failed executing {name}. Error: {e}", LogLevel.ERROR)
            take_screenshot(self.page, name)
            raise

    def click_element(self, locator: Locator):
        self.safe_execute(locator.click, 'click_element')

    def type_text(self, locator: Locator, text: str):
        self.safe_execute(locator.fill, 'type_text', text)

    def navigate_to(self, url: str):
        # Fixed: Added wait_until="commit" to bypass Facebook's background loading timeout
        self.safe_execute(self.page.goto, 'navigate_to', url, wait_until="commit")