import unittest
from datetime import time

import HtmlTestRunner

from Pages.Contactpage import Contactpage
from Pages.Loginpage import Loginpage
from TestUtility import XLUtils
from Testbase.Enviornmentsetup import Enviornmentsetup
from Configuration.Config import Config
import TestUtility.XLUtils
from TestUtility.XLUtils import readData
class Contact(Enviornmentsetup):

        def test_Contactpage(self):
            driver = self.driver
            driver.get(Config.URL)
            loginpg = Loginpage(driver)
            loginpg.enterusername(Config.usernameC)
            loginpg.enterpassword(Config.passwordC)
            loginpg.SubmitButton()

            Contactpg = Contactpage(driver)
            Contactpg.click_Contact()
            Contactpg.back_to_Home()
            Contactpg.Signoff_link


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Anupam\\PycharmProjects\\WebAppAutomation\\reports'))

