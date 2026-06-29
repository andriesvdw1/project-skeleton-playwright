import playwright
import logging
from python_project.helper.config import VALID_CREDENTIALS


def test_successfully_login(setup_load_page):
    login_page = setup_load_page
    login_page.perform_login(VALID_CREDENTIALS["username"], VALID_CREDENTIALS["password"])
