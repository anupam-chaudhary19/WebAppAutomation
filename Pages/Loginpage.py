from Locators import locator
from Locators.locator import Locators


class Loginpage():


    def __init__(self,driver):
        self.driver = driver

        self.username_textbox =Locators.username_textbox
        self.password_textbox = Locators.password_textbox
        self.login_button = Locators.login_button

    def enterusername(self, username):
        self.driver.find_element_by_name(self.username_textbox).clear()
        self.driver.find_element_by_name(self.username_textbox).send_keys(username)

    def enterpassword(self, password):
        self.driver.find_element_by_name(self.password_textbox).clear()
        self.driver.find_element_by_name(self.password_textbox).send_keys(password)

    def SubmitButton(self):
        self.driver.find_element_by_name(self.login_button).click()
