from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest
from AUTO.PageApp.loginPage import LoginPage
from AUTO.PageApp.searchPage import SearchPage
from AUTO.PageApp.quotePage import QuotePage
from AUTO.Data.database import Database
import xlrd
import HtmlTestRunner
import sys
import os
from selenium.common.exceptions import NoSuchElementException

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
data_input = int(input("|Ingresa la cantidad de iteraciones|:\n"))

# data_sheet = int(input("|Cotización|:\n"))

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
