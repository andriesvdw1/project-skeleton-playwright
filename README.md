## Tech stack
Playwright
Python
Pytest

App to test on: A locally hosted nodeJS http login form with a login page with a page that shows logged in and a page that shows invalid credentials.

## Setup Instructions
1. install dependence
    ```bash
   pip install -r requirements.txt
   playwright install
   
## Still in progress 
The goal of the project skeleton is to enable the testing of a login page that features username and password and a login button.
### Tests that will be available once completed:
Username valid, password vaild
Username valid, password invalid
Username invalid, password valid

Verify that the page changes from the login screen to the 'logged in' screen.
