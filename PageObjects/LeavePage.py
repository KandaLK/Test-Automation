# PageObjects/LeavePage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Leave:
    
    leave_header_xpath = "//h6[text()='Leave']"  # Match any heading containing "Leave"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Increased timeout when needed

    def isLeavePageDisplayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.leave_header_xpath)))
            return True  
            
        except Exception as e:
            print(f"Failed to verify My Leave page: {str(e)}")
            return False
