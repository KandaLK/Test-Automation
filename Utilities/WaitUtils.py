from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


# waitUtils.py
# This module contains utility functions for waiting for elements in Selenium WebDriver.    
# This is used to handle the parameters without hardcoding them in the test cases.

class WaitUtils:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = logging.getLogger(__name__)
    
    def wait_for_element_visible(self, locator_type, locator_value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((locator_type, locator_value)))
            return element
        except Exception as e:
            self.logger.error(f"Element not visible: {locator_value}, Error: {str(e)}")
            raise
    
    def wait_for_element_clickable(self, locator_type, locator_value):
        try:
            element = self.wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
            return element
        except Exception as e:
            self.logger.error(f"Element not clickable: {locator_value}, Error: {str(e)}")
            raise
