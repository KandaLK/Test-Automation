import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Use this fixture to set up the browser
# pytest will use this fixture to set up the browser before running tests  
# Can add preferred browsers without changing the test code

@pytest.fixture()
def setup(browser):
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
    )

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
