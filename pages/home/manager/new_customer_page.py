import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
from selenium import webdriver
import time



class NewCustomerPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _new_customer_link = "//a[contains(text(),'New Customer')]"
    _customer_name = "//input[@name='name']"
    _male_gender = "//input[@value='m']"
    _female_gender = "//input[@value='f']"
    _dob = "//input[@id='dob']"
    _street_address = "//textarea[@name='addr']"
    _city = "//input[@name='city']"
    _state = "//input[@name='state']"
    _pin = "//input[@name='pinno']"
    _mobile_number ="//input[@name='telephoneno']"
    _email = "//input[@name='emailid']"
    _password = "//input[@name='password']"
    _submit = "//input[@value='Submit']"
    _reset = "//input[@value='Reset']"

    def clickNewCustomer(self):
        self.elementClick(self._new_customer_link, locatorType="xpath")

    def enterCustomer(self, customername):
        self.sendKeys(customername, self._customer_name,locatorType="xpath")

    def chooseGender(self, gender="m"):
        elemale = self.driver.find_element_by_xpath(self._male_gender)
        elefem =  self.driver.find_element_by_xpath(self._female_gender)
        if gender == 'm':
            if elemale.is_selected:
                print("Male is selected")
            else:
                elemale.click()
                print("Male is now selected")
        else:
            elefem.click()
            print("Female is now selected")

    def enterStreet(self,street):
        self.sendKeys(street, self._street_address, locatorType="xpath")

    def enterDOB(self,birthdate):
        self.sendKeys(birthdate,self._dob,locatorType="xpath")

    def enterCity(self,city):
        self.sendKeys(city, self._city, locatorType="xpath")

    def enterState(self, state):
        self.sendKeys(state, self._state, locatorType="xpath")

    def enterPin(self,pin_num):
        self.sendKeys(pin_num, self._pin, locatorType="xpath")

    def enterMobile(self,mobile_num):
        self.sendKeys(mobile_num, self._mobile_number, locatorType="xpath")

    def enterEmail(self,email):
        self.sendKeys(email, self._email, locatorType="xpath")

    def enterPassword(self,password):
        self.sendKeys(password, self._password, locatorType="xpath")

    def submit_btn(self):
        self.elementClick(self._submit, locatorType="xpath")
        #Check if there is a alert present. If not. Skip check on alert text.
        #ADD code here.
        # Switch the control to the Alert window
        obj = self.driver.switch_to.alert

        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)

        time.sleep(2)

        # use the accept() method to accept the alert
        obj.accept()

        print(" Clicked on the OK Button in the Alert Window")

    def reset_btn(self):
        self.elementClick(self._reset, locatorType="xpath")

    def addNewCustomer(self, customer,gender,birthdate,street,city,state,pincode,mobile,email,password):
        self.enterCustomer(customer)
        self.chooseGender(gender)
        self.enterDOB(birthdate)
        self.enterStreet(street)
        self.enterCity(city)
        self.enterState(state)
        self.enterPin(pincode)
        self.enterMobile(mobile)
        self.enterEmail(email)
        self.enterPassword(password)




    # def enterAddress(self,street,city):


