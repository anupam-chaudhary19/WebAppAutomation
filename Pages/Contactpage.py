from Locators.locator import Locators
class Contactpage():

    def __init__(self, driver):
        self.driver=driver
        self.Contact_link = Locators.Contact_link
        self.backtohome = Locators.backtohome
        self.Signoff_link = Locators.Signoff_link

    def back_to_Home(self):
            self.driver.find_element_by_xpath(self.backtohome).click()

    def click_Contact(self):
        self.driver.find_element_by_xpath(self.Contact_link).click()