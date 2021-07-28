import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_login(self,setup):
        self.logger.info("************** Test_002_DDT_Login ************")
        self.logger.info("************** Verifying Login Test ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in an excel", self.rows)

        lst_status = []

        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path,'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r,3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass - Successfully logged in":
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail - Entered Invalid Credentials":
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    lst_status.append("Fail")
                elif self.exp == 'Fail - Entered Invalid Data':
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT Test Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT test failed *****")
            self.driver.close()
            assert False

        self.logger.info("***** END of Login DDT Test ******")
        self.logger.info("***** Completed Test_002_DDT_Login TC *****")