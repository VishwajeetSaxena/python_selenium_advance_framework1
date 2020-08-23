import time

from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _login_link = "Login"
    _user_email = "user_email"
    _user_password = "user_password"
    _submit_button = "commit"

    # Get the objects
    def get_login_link(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)

    def get_user_email(self):
        return self.driver.find_element(By.ID, self._user_email)

    def get_user_password(self):
        return self.driver.find_element(By.ID, self._user_password)

    def get_submit_button(self):
        return self.driver.find_element(By.NAME, self._submit_button)

    # Perform action on the object

    def click_login_link(self):
        self.get_login_link().click()

    def send_user_email(self, username):
        self.get_user_email().send_keys(username)

    def send_user_password(self, password):
        self.get_user_password().send_keys(password)

    def click_submit_button(self):
        self.get_submit_button().click()

    # Calling function, to be called from test case
    def login(self, username, password):
        self.click_login_link()
        time.sleep(30)
        self.send_user_email(username)
        self.send_user_password(password)
        self.click_submit_button()
