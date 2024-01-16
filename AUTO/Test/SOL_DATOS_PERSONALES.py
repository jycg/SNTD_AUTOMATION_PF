import unittest
import re
import time
import sys
import os
import xlrd
import logging
import traceback
from datetime import datetime
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from AUTO.PageApp.loginPage import LoginPage
from AUTO.PageApp.searchPage import SearchPage
from AUTO.PageApp.quotePage import QuotePage
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from AUTO.Locator.locators import Locators
from selenium.webdriver.edge.options import Options


class MyTestCaseSolicitud(unittest.TestCase):
    driver = None

    @classmethod
    def datos_personales(cls):
        print("Ejemplo de una función diferente en diferente archivo")


if __name__ == '__main__':
    unittest.main()
