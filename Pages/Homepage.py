from Locators.locator import Locators
class Homepage():

    def __init__(self, driver):
        self.driver = driver
        self.Itinerary_link = Locators.Itinerary_link
        self.Signoff_link = Locators.Signoff_link
        self.Profile_link = Locators.Profile_link
        self.Support_link = Locators.Support_link
        self.Contact_link = Locators.Contact_link


    def click_Itinerary(self):
        self.driver.find_element_by_id(self.Itinerary_link).click()

    def click_Signoff(self):
        self.driver.find_element_by_xpath(self.Signoff_link).click()

    def click_Profile(self):
        self.driver.find_element_by_id(self.Profile_link).click()

    def click_Support(self):
        self.driver.find_element_by_id(self.Support_link).click()

    def click_Contact(self):
        self.driver.find_element_by_xpath(self.Contact_link).click()

