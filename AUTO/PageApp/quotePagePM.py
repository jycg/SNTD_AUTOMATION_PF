from selenium.webdriver.common.by import By
from AUTO.Locator.locators_PM import LocatorsPM
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from AUTO.Data.database import Database
import xlrd
class QuotePagePM():

    def __init__(self, driver):
        self.driver = driver

    def clic_nvaCot(self):
        self.driver.find_element(By.XPATH, LocatorsPM.btn_nvaCot).click()
    def clic_product_n(self):
        self.driver.find_element(By.XPATH, LocatorsPM.producto_n).click()
    def clic_marca(self):
        self.driver.find_element(By.XPATH, LocatorsPM.marca).click()
    def enter_marca(self, marca_send):
        self.driver.find_element(By.XPATH, LocatorsPM.marca_send).send_keys(marca_send)
    def enter_marca1(self):
        self.driver.find_element(By.XPATH, LocatorsPM.marca).send_keys(Keys.ENTER)