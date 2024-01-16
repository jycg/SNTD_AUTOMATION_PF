from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from AUTO.PageApp.loginPage import LoginPage
from AUTO.PageApp.searchPage import SearchPage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s=Service("C:/Users/jgarcia/PycharmProjects/SNTDProject/drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://sntdtest.tekprovider.net:9444/TekFinauto/Autogestion/Acceso/Login")

        login = LoginPage(driver)
        login.enter_username("TBBT01")
        login.enter_password("S1santan")
        login.click_login()

        search = SearchPage(driver)
        search.click_ausername()
        search.click_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test complete")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/jgarcia/PycharmProjects/SNTDProject/AUTO/reports'))