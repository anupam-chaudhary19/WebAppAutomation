from distutils.log import Log
from selenium import webdriver
import time
import unittest
import sys
import os

from selenium.webdriver.common import alert

import TestUtility.XLUtils
from TestUtility import XLUtils
from TestUtility.Screenshot import screenshotss

sys.path.append(os.path.join(os.path.dirname(__file__), "......", "......"))
from Pages.Homepage import Homepage
from Pages.Loginpage import Loginpage
from Pages.Contactpage import Contactpage
from Configuration.Config import Config
from Testbase.Enviornmentsetup import Enviornmentsetup
import HtmlTestRunner

path = "C:/Users/Anupam/PycharmProjects/WebAppAutomation/TestUtility/login.xlsx"
rows = XLUtils.getRowCount(path, 'Sheet1')

class Logintest(Enviornmentsetup):

    def test_Loginvalid(self):
        driver= self.driver
        driver.get(Config.URL)
        loginpg = Loginpage(driver)
        Homepg = Homepage(driver)

        for r in range(2, rows + 1):
            username = XLUtils.readData(path, "Sheet1", r, 1)
            password = XLUtils.readData(path, "Sheet1", r, 2)
            loginpg.enterusername(username)
            loginpg.enterpassword(password)
            loginpg.SubmitButton()
            time.sleep(9)
            driver.save_screenshot("C:/Users/Anupam/PycharmProjects/WebAppAutomation/TestUtility/homepage.png")
            if driver.title=="Find a Flight: Mercury Tours:":
                print("Test passed")
                XLUtils.writeData(path, "Sheet1", r, 3, "Test passed")
                #Userc=username
                #PassC=password
                Homepg.click_Signoff()
            else:
                print("Test failed")
                XLUtils.writeData(path, "Sheet1", r, 3, "Test failed")

        time.sleep(10)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Anupam\\PycharmProjects\\WebAppAutomation\\reports'))
    #   Homepg =Homepage(driver)
     #   Homepg.click_Contact()

      #  Contactpg =Contactpage(driver)
      #  Contactpg.back_to_Home()

      #  Homepg.click_Signoff()
       # self.driver.get("http://newtours.demoaut.com/mercurysignon.php")
       # self.driver.find_element_by_name("userName").send_keys("automationscript")
       # self.driver.find_element_by_name("password").send_keys("Zxcv@1234")
       # self.driver.find_element_by_name("login").click()