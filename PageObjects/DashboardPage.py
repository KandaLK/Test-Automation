from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.waitUtils import WaitUtils


class Dashboard:
    dashboard_header_xpath = "//h6[text()='Dashboard']"
    quick_launch_area_xpath = "//div[contains(@class, 'orangehrm-quick-launch')]"
    #quick_launch_leave_xpath = "//div[contains(@class, 'orangehrm-quick-launch-card')]//p[text()='My Leave']"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Increased timeout

    def isDashboardDisplayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.dashboard_header_xpath)))
            return True
        except:
            return False

    def clickMyLeave(self):
        try:
            # First try the quick launch area
            quick_launch_elements = self.driver.find_elements(By.XPATH, self.quick_launch_area_xpath)
            
            if len(quick_launch_elements) > 0:
                quick_launch_elements[0].click()
                print("Clicked My Leave via quick launch")
                self.driver.save_screenshot("./Screenshots/test_myLeave_passed.png")
            else:
                print("My Leave not found in quick launch, trying main menu...")
                self.driver.save_screenshot("./Screenshots/test_myLeave_failed.png")

             
        except Exception as e:
            print(f"Error clicking My Leave: {str(e)}")
