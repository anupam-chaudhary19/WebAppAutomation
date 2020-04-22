import unittest
import string
from random import randint, random

import HtmlTestRunner
from Pages.Loginpage import Loginpage
from Pages.Register import Register
from Configuration.Functions import functions
from Configuration.Config import Config
from Testbase.DynamicFunction import randomString, randomStringwithDigitsAndSymbols, random_secure_string, randomNumber
from Testbase.Enviornmentsetup import Enviornmentsetup


class Registerpg(Enviornmentsetup):
    def test_Registerpage(self):
        driver = self.driver
        driver.get(Config.URL)
        '''loginpg = Loginpage(driver)
        loginpg.enterusername(Config.usernameC)
        loginpg.enterpassword(Config.passwordC)
        loginpg.SubmitButton()'''

        Registerpg = Register(driver)
        Registerpg.RegisterButton()
        Registerpg.enterFirstname(randomString())
        Registerpg.enterLastname(randomString())
        Registerpg.PhoneNumber(9979797979)
        Registerpg.Email(randomStringwithDigitsAndSymbols())
        Registerpg.Address(randomStringwithDigitsAndSymbols)
        Registerpg.City(randomString())
        Registerpg.State_Province(randomString())
        Registerpg.Postal_Code(random.range(10000,90000))
        Registerpg.Username_textbox(randomString())
        Registerpg.Password_textbox(random_secure_string)
        Registerpg.ConfirmPassword_textbox(random_secure_string)


if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Anupam\\PycharmProjects\\WebAppAutomation\\reports'))