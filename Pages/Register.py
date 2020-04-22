from Locators.locator import Locators
class Register():

    def __init__(self, driver):
        self.driver= driver
        self.Firstname_txtbox = Locators.Firstname_textbox
        self.Lastname_txtbox = Locators.Lastname_textbox
        self.PhoneNumber = Locators.PhoneNumber
        self.Email= Locators.Email
        self.Address= Locators.Address
        self.City= Locators.City
        self.State_Province= Locators.State_Province
        self.Postal_Code= Locators.Postal_Code
        self.Username_textbox=  Locators.Username_textbox
        self.Password_textbox= Locators.Password_textbox
        self.Country_dropdwon = Locators.Country
        self.ConfirmPassword_textbox= Locators.ConfirmPassword_textbox
        self.Register_btn= Locators.Register_link
        self.Signoff_link = Locators.Signoff_link


    def enterFirstname(self, Firstname):
        self.driver.find_element_by_name(self.Firstname_txtbox).clear()
        self.driver.find_element_by_name(self.Firstname_txtbox).send_keys(Firstname)

    def enterLastname(self, Lastname):
        self.driver.find_element_by_name(self.Lastname_txtbox).clear()
        self.driver.find_element_by_name(self.Lastname_txtbox).send_keys(Lastname)

    def enterPhonenumber(self, PhoneNumber):
        self.driver.find_element_by_name(self.PhoneNumber).clear()
        self.driver.find_element_by_name(self.PhoneNumber).send_keys(PhoneNumber)

    def enterEmail_id(self, Emailid):
        self.driver.find_element_by_name(self.Email).clear()
        self.driver.find_element_by_name(self.Email).send_keys(Emailid)

    def enterCity(self, city):
        self.driver.find_element_by_name(self.City).clear()
        self.driver.find_element_by_name(self.City).send_keys(city)

    def enterAddress(self, Address):
        self.driver.find_element_by_name(self.Address).clear()
        self.driver.find_element_by_name(self.Address).send_keys(Address)

    def enterState_Province(self, State):
        self.driver.find_element_by_name(self.State_Province).clear()
        self.driver.find_element_by_name(self.State_Province).send_keys(State)

    def enter_Postalcode(self, Code):
        self.driver.find_element_by_name(self.Postal_Code).clear()
        self.driver.find_element_by_name(self.Postal_Code).send_keys(Code)

    def enter_Usernametxtbox(self, Username):
        self.driver.find_element_by_name(self.Username_textbox).clear()
        self.driver.find_element_by_name(self.Username_textbox).send_keys(Username)

    def enter_Passwordtxtbox(self, Password):
        self.driver.find_element_by_name(self.Password_textbox).clear()
        self.driver.find_element_by_name(self.Password_textbox).send_keys(Password)

    def enter_Confirmpassword(self, Cpassword):
        self.driver.find_element_by_name(self.ConfirmPassword_textbox).clear()
        self.driver.find_element_by_name(self.ConfirmPassword_textbox).send_keys(Cpassword)

    #def enter_Country_Dropdown(self):
       # Select dp = self.driver.find_element_by_name(self.Country_dropdwon)


    def RegisterButton(self):
        self.driver.find_element_by_xpath(self.Register_btn).click()

        #         COUNYTY DROPDOWN ADD KARNA HAI