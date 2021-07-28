from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Eclipse-Selenium\chromedriver_win32\chromedriver.exe")
        print("Launching Chrome Browser.........")
    elif browser == 'firefox':
        driver=webdriver.Firefox(executable_path="C:\Program Files (x86)\Eclipse-Selenium\geckodriver-v0.29.1-win64\geckodriver.exe")
        print("Launching Firefox Browser.........")
    else:
        driver=webdriver.Ie(executable_path="C:\Program Files (x86)\Eclipse-Selenium\IEDriverServer_x64_3.150.1\IEDriverServer.exe")
    return driver

def pytest_addoption(parser): # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # # This will return the Browser value to setup method
    return request.config.getoption("--browser")

######### PyTest HTML Reports ##########
# It is a hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Srinivas'

# It is a hook for del/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadeta(metadeta):
    metadeta.pop("JAVA_HOME", None)
    metadeta.pop("Plugins", None)


######## COMMANDS to RUN in TERMINAL #########
# 1) pytest -v -s testCases/test_login.py --browser chrome
# 2) pytest -v -s testCases/test_login.py --browser firefox
# 3) pytest -v -s testCases/test_login.py --browser Ie
# 4) pytest -v -s -n=2 testCases/test_login.py --browser chrome >>> Runs 2 test methods parallely in 2 chrome tabs