from selenium import webdriver
import pytest



@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("launching chrome browser.............")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("launching fire fox browser...........")
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name'] =' Fazlul_Selenium_Project'
    config._metadata['Module Name']  = ' login page'
    config._metadata['Tester'] = 'Fazlul'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME",None)
    metadata.pop("Plugins", None)