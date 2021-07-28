import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homepage_title(self,setup):
        self.logger.info("************** Test_001_Login ************")
        self.logger.info("************** Verifying Homepage Title ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.logger.info("************ Home page title test is passed ***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            self.logger.error("************ Home page title test is failed ***********")
            assert False

    def test_login(self,setup):
        self.logger.info("************** Verifying Login Test ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************ Login page test is passed ***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************ Login page test is failed ***********")
            assert False