from selenium import webdriver
from selenium.webdriver.common.by import By
from AUTO.Locator.locators_PM import LocatorsPM
class MenuPage():

    def __init__(self, driver):
        self.driver = driver

    def clic_menu(self):
        self.driver.find_element(By.XPATH, LocatorsPM.icono_menu).click()
    def clic_cotPM(self):
        self.driver.find_element(By.XPATH, LocatorsPM.menu_pm).click()
    # def enter_password(self, password):
    #     self.driver.find_element(By.ID, Locators.pass_autogestion).clear()
    #     self.driver.find_element(By.ID, Locators.pass_autogestion).send_keys(password)
    #
    # def click_login(self):
    #     self.driver.find_element(By.ID, Locators.login_autogestion).click()