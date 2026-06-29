import playwright
import logging
from python_project.helper.config import VALID_CREDENTIALS


def test_successfully_login(setup_load_page):
    login_page = setup_load_page
    login_page.perform_login(VALID_CREDENTIALS["email"], VALID_CREDENTIALS["password"])


# open browser and load the login page
# username entered
# password entered
# click login button
# verify logged in successfully

#test 2
#[wrong username, valid password]
#[valid username, wrong password]
#[missing username, valid password]
#[valid username, missing password]

# open browser and load the login page
# enter test case
# press login
# verify failed login