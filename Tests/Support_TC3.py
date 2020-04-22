import unittest

import HtmlTestRunner

from Pages.Loginpage import Loginpage
from Pages.Supportpage import Supportpage
from Testbase.Enviornmentsetup import Enviornmentsetup
from Configuration.Config import Config
class Supportpg():

    def __init__(self, driver):
        self.driver= driver

        driver.get(Config.URL)
        loginpg = Loginpage(driver)
        loginpg.enterusername(Config.username)
        loginpg.enterpassword(Config.password)
        loginpg.SubmitButton()

        Supportpg = Supportpage(driver)
        Supportpg.click_Support()
        Supportpg.backtohome
        Supportpg.Signoff_link

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:\\Users\\Anupam\\PycharmProjects\\WebAppAutomation\\reports'))
