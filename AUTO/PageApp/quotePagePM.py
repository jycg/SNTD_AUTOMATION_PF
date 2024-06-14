from selenium.webdriver.common.by import By
from AUTO.Locator.locators_PM import LocatorsPM
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

class QuotePagePM:

    def __init__(self, driver):
        self.driver = driver

    def menu_pm(self):
        self.driver.find_element(By.XPATH, LocatorsPM.clic_menu_pm).click()

    def menu_pm_2(self):
        self.driver.find_element(By.XPATH, LocatorsPM.menu_pm).click()

    def clic_nvaCot(self):
        self.driver.find_element(By.XPATH, LocatorsPM.btn_nvaCot).click()

    def clic_product_n(self):
        self.driver.find_element(By.XPATH, LocatorsPM.producto_n).click()

    def clic_marca(self):
        self.driver.find_element(By.XPATH, LocatorsPM.marca_pm).click()

    def enter_marca(self, marca_send):
        self.driver.find_element(By.XPATH, LocatorsPM.marca_pm_2).send_keys(marca_send)
        self.driver.find_element(By.XPATH, LocatorsPM.marca_pm_2).send_keys(Keys.ENTER)

    def enter_marca1(self):
        self.driver.find_element(By.XPATH, LocatorsPM.marca).send_keys(Keys.ENTER)
