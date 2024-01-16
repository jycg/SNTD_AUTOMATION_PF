from selenium.webdriver.common.by import By
from AUTO.Locator.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, Locators.usuario_autogestion).clear()
        self.driver.find_element(By.ID, Locators.usuario_autogestion).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, Locators.pass_autogestion).clear()
        self.driver.find_element(By.ID, Locators.pass_autogestion).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, Locators.login_autogestion).click()
