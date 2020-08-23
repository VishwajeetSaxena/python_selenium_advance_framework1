from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox(executable_path='C:\\Users\\91897\\python_selenium_advance_framework1\\python_selenium_advance_framework1\\utilities\\sel_drivers\\geckodriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        driver.quit()

