import time
from traceback import print_stack

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Selenium_Custom():

    # constructor
    def __init__(self, driver):
        self.driver = driver


    # Get element

    def updated_locator_type(self, locator_type):
        locator_type = str(locator_type).lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'tag_name':
            return By.TAG_NAME
        elif locator_type == 'class_name':
            return By.CLASS_NAME
        elif locator_type == 'partial_link_text':
            return By.PARTIAL_LINK_TEXT
        elif locator_type == 'link_text':
            return By.LINK_TEXT
        elif locator_type == 'css_selector':
            return By.CSS_SELECTOR
        else:
            print("Locator type " + locator_type + " not correct/supported")

    def get_element(self, locator_value , locator_type='xpath'):
        try:
            locator_type = self.updated_locator_type(locator_type)
            element = self.driver.find_element(locator_type, locator_value)
            return element
        except:
            print("No such element found")

    def get_elements(self, locator_value, locator_type='xpath'):
        try:
            locator_type = self.updated_locator_type(locator_type)
            elements = self.driver.find_elements(locator_type, locator_value)
            return elements
        except:
            print("No such element found")



    # Custom methods

    def element_click(self, locator, locatorType="xpath"):
        try:
            element = self.get_element(locator, locatorType)
            element.click()
            print("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            print("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()


    def element_send_keys(self, data, locator, locatorType="xpath"):
        try:
            element = self.get_element(locator, locatorType)
            element.send_keys(data)
            print("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def check_element_present(self, locator_value, locator_type='xpath'):
        try:
            locator_type = self.updated_locator_type(locator_type)
            element = self.driver.find_element(locator_type, locator_value)

            if element is not None:
                return True
            else:
                return False

        except:
            print("No such element found")
            return False

    def check_elements_present(self, locator_value, locator_type='xpath'):
        try:
            locator_type = self.updated_locator_type(locator_type)
            elements = self.driver.find_elements(locator_type, locator_value)

            if len(elements) > 0:
                return True
            else:
                return False
        except:
            print("No such element found")
            return False

    def wait_until_element_present(self, locator_value, action_type, locator_type='xpath', driver_timeout=10, poll_frequency=1):
        try:
            locator_type = self.updated_locator_type(locator_type)

            wait = WebDriverWait(self.driver, driver_timeout, poll_frequency, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            if action_type == 'click':
                element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='benzradio']")))
                return element
            elif action_type == 'select':
                element = wait.until(
                expected_conditions.element_to_be_selected(locator_type, locator_value))
                return element
            else:
                print('action type not matched with the available options')
        except:
            print("No such element found")
            return False

    def take_screenshot(self):
        try:
            dir = "C:\\Users\\91897\\workspace_python\\screenshot_dir\\"
            file_name = str(round(time.time() * 1000)) + '.png'
            file = dir + file_name
            self.driver.save_screenshot(file)
            time.sleep(2)
            print("Screenshot taken successfully")
            return file
        except:
            print("Unable to take screenshot")
            return False
