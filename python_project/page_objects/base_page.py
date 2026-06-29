import logging  # Fixed: Added missing import
from playwright.sync_api import Page, Locator
from python_project.helper.utils import LogLevel, take_screenshot


# Note: Ensure that whatever provides 'log.message' is imported here if it's a custom helper.
# If you don't have a custom 'log' module, you can use self.logger directly (see alternative below).


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)

    def safe_execute(self, action, action_name: str, *args):
        try:
            # Assuming 'log' is an imported helper utility from your framework
            # Fixed alternative if 'log' doesn't exist: self.logger.info(f"Executing...")
            self.logger.info(f"Executing {action_name} with arguments {args}")
            action(*args)
        except Exception as e:
            self.logger.error(f"Failed executing {action_name} with arguments {args}. Error: {e}")
            take_screenshot(self.page, action_name)
            raise

    def click_element(self, locator: Locator):
        self.safe_execute(locator.click, 'click_element')

    def type_text(self, locator: Locator, text: str):
        self.safe_execute(locator.fill, 'type_text', text)

    def navigate_to(self, url: str):
        self.safe_execute(self.page.goto, 'navigate_to', url)