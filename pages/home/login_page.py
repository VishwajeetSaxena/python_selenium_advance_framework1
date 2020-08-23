import time

from selenium.webdriver.common.by import By
from base.selenium_custom_methods import Selenium_Custom

class LoginPage(Selenium_Custom):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _user_email = "user_email"
    _user_password = "user_password"
    _submit_button = "commit"

    # Perform action on the object

    def click_login_link(self):
        self.element_click(self._login_link, 'LINK_TEXT')

    def send_user_email(self, username):
        self.element_send_keys(username, self._user_email, 'ID')

    def send_user_password(self, password):
        self.element_send_keys(password, self._user_password, 'ID')

    def click_submit_button(self):
        self.element_click(self._submit_button, 'name')

    # Calling function, to be called from test case
    def login(self, username, password):
        self.click_login_link()
        time.sleep(30)
        self.send_user_email(username)
        self.send_user_password(password)
        self.click_submit_button()
