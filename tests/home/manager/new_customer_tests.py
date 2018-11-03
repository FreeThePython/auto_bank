from pages.home.login_page import LoginPage
from pages.home.manager.new_customer_page import NewCustomerPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt # used for data driven testing from CSV
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nc = NewCustomerPage(self.driver)

    # @data(*getCSVData("testdata.csv"))
    # @unpack
    # @pytest.mark.run(order=2)
    # def test_AddNewCustomersFile(self,Customer,Gender,DOB,Street,City,State,Pincode,Mobile,Email,Password):
    #     self.lp.login("mngr160862", "sAqUneg")
    #     self.nc.clickNewCustomer()
    #     self.nc.addNewCustomer(customer=Customer, gender=Gender,
    #                            birthdate=DOB, street= Street,
    #                            city=City, state= State, pincode=Pincode,
    #                            mobile=Mobile, email=Email,password=Password)
    #     self.nc.submit_btn()

        #time.sleep(3)

        # result2 = self.lp.verifyLoginSuccessful()
        # self.ts.markFinal("test_validLogin", result2, "Login Verification")

    @pytest.mark.run(order=1)
    def test_AddOneNewCustomersFile(self):
        self.lp.login("mngr160862", "sAqUneg")
        self.nc.clickNewCustomer()
        self.nc.addNewCustomer("Rick Grimes",'m', "12251960", "451 Farout Rd", "Newton",
                               "New Hampshire", "357800", "9119119191", "justone777@gmail.com", "adsrgdfbvad")
        time.sleep(3)
        self.nc.submit_btn()