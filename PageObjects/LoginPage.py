from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    text_box_username_name = "username"
    text_box_password_name = "password"
    btn_login_xpath = '//*[@type="submit"]'
    link_Tab_xpath = "//span[@class='oxd-userdropdown-tab']"
    link_logout_xpath = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def getTitle(self):
        return self.driver.title

    def setUsername(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, self.text_box_username_name))
        )
        username_field.clear()
        username_field.send_keys(username)

    def setPassword(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, self.text_box_password_name))
        )
        password_field.clear()
        password_field.send_keys(password)

    def clickLogin(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.btn_login_xpath))
        )
        login_button.click()

    def clickLogout(self):
        welcome_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.link_Tab_xpath))
        )
        welcome_link.click()
        logout_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.link_logout_xpath))
        )
        logout_link.click()
