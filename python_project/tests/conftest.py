import pytest


from python_project.helper.config import URL
from python_project.helper.utils import LogLevel, log_message
from python_project.page_objects.login_page import LoginPage
import logging

@pytest.fixture()
def setup_playwright(playwright, request):
    headed = request.config.getoption("--headed", default=False)
    browser = playwright.chromium.launch(headless=not headed)
    page = browser.new_page()
    try:
        yield page
    finally:
        log_message(logging.getLogger(), "closing browser", LogLevel.INFO)
        browser.close()


@pytest.fixture()
def setup_load_page(setup_playwright):
    login_page = LoginPage(setup_playwright)
    login_page.navigate_to(URL)
    log_message(logging.getLogger(), f"navigate to {URL}", LogLevel.INFO)

    return login_page  # <-- Add this line to pass the object to your test!
