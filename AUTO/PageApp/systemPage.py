from selenium.webdriver.common.by import By
from AUTO.Locator.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import xlrd
class Systempage():

    def __init__(self, driver):

        self.driver = driver

    # PRODUCTO
    def scroll_page(self):
        self.driver.execute
        self.driver.find_element(By.XPATH, Locators.producto_credito).click()