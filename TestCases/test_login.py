import pytest
from Utilities.WaitUtils import WaitUtils
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import Dashboard
from Utilities.ReadProperties import ReadConfig
from Utilities.Logger import LogGen

#Test case class for login functionality 
#Tittle and login test cases

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    

    def test_homePageTitle(self, setup):
        self.logger.info("*** Test_01_Login ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wait_utils = WaitUtils(self.driver)

        actual_title = self.driver.title
        if "OrangeHRM" in actual_title:
            self.logger.info("*** Home page title test passed ***")
            assert True
        else:
            self.logger.error("**** Home page title test failed ****")
            self.driver.save_screenshot("./Screenshots/test_homePageTitle_failed.png")
            assert False


    def test_login(self, setup):
        self.logger.info("*** Started Login Test ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wait_utils = WaitUtils(self.driver)

        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.wait_utils = WaitUtils(self.driver)

        self.dashboard = Dashboard(self.driver)
        if self.dashboard.isDashboardDisplayed():
            self.logger.info("*** Login test passed - Dashboard verified ***")
            assert True
        else:
            self.logger.error("*** Login test failed - Dashboard not found! ***")
            self.driver.save_screenshot("./Screenshots/test_login_failed.png")
            assert False
