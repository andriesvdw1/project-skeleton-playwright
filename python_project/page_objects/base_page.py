from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # 3. Rename the first parameter to 'action' so action(*args) works
    def safe_execute(self, action, action_name: str, *args):
        try:
            print(f"Executing: {action_name}")  # log
            action(*args)
        except Exception as e:
            print(f"Error in {action_name}: {e}")  # log
            # self.page.screenshot(path=f"{action_name}_error.png")  # take screenshot
            raise

    def click_element(self, locator: Locator):
        # 2. Pass the method, the log name, then any arguments the method needs
        self.safe_execute(locator.click, 'click_element')

    def type_text(self, locator: Locator, text: str):
        # 2. Pass 'text' at the very end so it gets bundled into *args
        self.safe_execute(locator.fill, 'type_text', text)

    def navigate_to(self, url: str):
        # 1. Pass the method itself (self.page.goto), NOT the result of calling it
        self.safe_execute(self.page.goto, 'navigate_to', url)