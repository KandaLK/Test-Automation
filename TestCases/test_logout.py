import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from Utilities.ReadProperties import ReadConfig
from Utilities.Logger import LogGen
from Utilities.WaitUtils import WaitUtils

class Test_003_Logout:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    
    def test_logout(self, setup):
        self.logger.info("***  Test_03_Logout  ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wait = WaitUtils(self.driver)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.wait = WaitUtils(self.driver)
        self.lp.clickLogout()

        try:
            login_button = self.driver.find_element(By.XPATH, self.lp.btn_login_xpath)
            if login_button.is_displayed():
                self.logger.info("*** Logout test passed - Login page verified ***")
                #self.driver.save_screenshot("./OrangeHRM_Automation/Screenshots/test_logout_passed.png")
                assert True
            else:
                self.logger.error("*** Logout test failed - Login page not displayed  ***")
                self.driver.save_screenshot("./Screenshots/test_logout_failed.png")
                assert False
        except:
            self.logger.error("*** Logout test failed - Login button not found ***")
            self.driver.save_screenshot("./Screenshots/test_logout_failed.png")
            assert False
