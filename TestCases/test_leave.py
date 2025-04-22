from Utilities.WaitUtils import WaitUtils
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import Dashboard
from PageObjects.LeavePage import Leave
from Utilities.ReadProperties import ReadConfig
from Utilities.Logger import LogGen

# MY LEAVE PAGE TEST CASE 
# This test case verifies the functionality of the My Leave page in the OrangeHRM application.
# It includes logging in, navigating to the My Leave page, and checking if the page loads correctly.

class Test_2_Leave:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    

    def test_leaveFunction(self, setup):
        self.logger.info("*** Test_02_Leave Page **")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.wait = WaitUtils(self.driver)
        
        # Login
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.wait = WaitUtils(self.driver)
        
        
        # Verify login success
        self.dashboard = Dashboard(self.driver)
        if not self.dashboard.isDashboardDisplayed():
            self.logger.error("*** Login failed, cannot proceed with leave test **")
            self.driver.save_screenshot("./Screenshots/login_failed_in_leave_test.png")
            assert False
        
        # Click on My Leave
        self.logger.info("*** Clicking on My Leave **")
        self.dashboard.clickMyLeave()
        self.wait = WaitUtils(self.driver)

        # Verify Leave page
        self.leave = Leave(self.driver)
        if self.leave.isLeavePageDisplayed():
            self.logger.info("*** Leave page load test passed ***")
            assert True
        else:
            self.logger.error("*** Leave page load test failed ***")
            self.driver.save_screenshot("./Screenshots/test_leaveFunction_failed.png")
            assert False


