from selenium.webdriver.common.by import By
from AUTO.Locator.locators import Locators
class SearchPage():

    def __init__(self, driver):
        self.driver = driver

    def click_ausername(self):
        self.driver.find_element(By.ID, Locators.usuario_busqueda).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, Locators.icono_salir).click()

    def click_nvaCot(self):
        self.driver.find_element(By.ID, Locators.nva_cot).click()