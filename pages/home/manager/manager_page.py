import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re



class ManagerPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _new_customer_link = "//a[contains(text(),'New Customer')]"
    _edit_customer_link ="//a[contains(text(),'Edit Customer')]"
    _delete_customer_link ="//a[@href='DeleteCustomerInput.php']"
    _new_account_link ="//a[contains(text(),'New Account')]"
    _edit_account_link ="//a[contains(text(),'Edit Account')]"
    _delete_account_link ="//a[contains(text(),'Edit Account')]"
    _deposit_link = "//a[contains(text(),'Deposit')]"
    _withdrawl_link ="//a[contains(text(),'Withdrawal')]"
    _fund_transfer_link ="//a[contains(text(),'Fund Transfer')]"
    _change_password_link ="//a[contains(text(),'Change Password')]"
    _balance_enquiry_link ="//a[contains(text(),'Balance Enquiry')]"
    _mini_statement_link = "//a[contains(text(),'Mini Statement')]"
    _customized_statement_link ="//a[contains(text(),'Customised Statement')]"
    _log_out_link ="//a[contains(text(),'Log out')]"







    def clickNewCustomer(self):
        self.elementClick(self._new_customer_link, locatorType="xpath")

    def clickEditCustomer(self):
        self.elementClick(self._edit_customer_link, locatorType="xpath")

    def clickDeleteCustomer(self):
        self.elementClick(self._delete_customer_link, locatorType="xpath")

    def clickNewAccount(self):
        self.elementClick(self._new_account_link, locatorType="xpath")

    def clickEditAccount(self):
        self.elementClick(self._edit_account_link, locatorType="xpath")

    def clickDeleteAccount(self):
        self.elementClick(self._delete_account_link, locatorType="xpath")

    def clickDeposit(self):
        self.elementClick(self._deposit_link, locatorType="xpath")

    def clickWithdrawal(self):
        self.elementClick(self._withdrawl_link, locatorType="xpath")

    def clickFundTransfer(self):
        self.elementClick(self._fund_transfer_link, locatorType="xpath")

    def clickChangePassword(self):
        self.elementClick(self._change_password_link, locatorType="xpath")

    def clickBalanceEnquiry(self):
        self.elementClick(self._balance_enquiry_link, locatorType="xpath")

    def clickMiniStatement(self):
        self.elementClick(self._mini_statement_link, locatorType="xpath")

    def clickCustomizedStatement(self):
        self.elementClick(self._customized_statement_link, locatorType="xpath")

    def clickLogout(self):
        self.elementClick(self._log_out_link, locatorType="xpath")