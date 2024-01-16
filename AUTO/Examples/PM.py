import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from AUTO.PageApp.loginPage import LoginPage
from AUTO.PageApp.menuPage import MenuPage
from AUTO.PageApp.quotePagePM import QuotePagePM
from AUTO.Data.database import Database
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd
import HtmlTestRunner
import sys
import os
from selenium.common.exceptions import NoSuchElementException


class MyTestCase(unittest.TestCase):
    @classmethod

    def setUpClass(cls):
        s = Service("C:/Users/jgarcia/PycharmProjects/SNTDProject/drivers/114/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        database = Database()
        driver = self.driver
        driver.get("https://sntdqa.tekprovider.net:9081/TekFinauto/Autogestion/Acceso/Login")

        login = LoginPage(driver)
        login.enter_username("TBBT01")
        login.enter_password("S1santan")
        login.click_login()

        menu = MenuPage(driver)
        time.sleep(3)
        menu.clic_menu()
        time.sleep(1)
        menu.clic_cotPM()
        time.sleep(2)

        quotepm = QuotePagePM(driver)
        quotepm.clic_nvaCot()
        time.sleep(1)
        quotepm.clic_product_n()
        time.sleep(2)
        quotepm.clic_marca()
        time.sleep(3)
        quotepm.enter_marca("KIA")
        # time.sleep(1)
        # quotepm.enter_marca1()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
        cls.driver.quit()
        print("Test complete")


if __name__ == '__main__':
    unittest.main()
