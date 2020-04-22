from Locators.locator import Locators
class Supportpage():
    def __init__(self, driver):
        self.driver = driver;

        self.Support_link = Locators.Support_link
        self.backtohome = Locators.backtohome
        self.Signoff_link = Locators.Signoff_link

    def click_Support(self):
        self.driver.find_element_by_id(self.Support_link).click()

    def back_to_Home(self):
            self.driver.find_element_by_xpath(self.backtohome).click()

    def click_Signoff(self):
        self.driver.find_element_by_xpath(self.Signoff_link).click()
