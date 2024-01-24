from AUTO.Locator.locators_solicitud import Locatorsolicitud
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SolicitudPage:
    def __init__(self, driver):
        self.driver = driver

    def click_client_sntd(self):
        self.driver.find_element(By.XPATH, Locatorsolicitud.dp_clientesntd).click()

    def enter_buc(self, sntdbuc):
        self.driver.find_element(By.ID, Locatorsolicitud.dp_txtBUC).send_keys(sntdbuc, Keys.ENTER)

    def click_sexo_hombre(self):
        self.driver.find_element(By.XPATH, Locatorsolicitud.dp_hombre).click()

    def click_sexo_mujer(self):
        self.driver.find_element(By.XPATH, Locatorsolicitud.dp_mujer).click()

    def enter_fecha(self, birthday):
        self.driver.find_element(By.ID, Locatorsolicitud.dp_fecha).click()
        self.driver.find_element(By.ID, Locatorsolicitud.dp_fecha).send_keys(Keys.CONTROL + "A")
        self.driver.find_element(By.ID, Locatorsolicitud.dp_fecha).send_keys(Keys.CLEAR)
        self.driver.find_element(By.ID, Locatorsolicitud.dp_fecha).send_keys(birthday)

    def click_entidad_nac(self, entidadnac):
        select_entidad_nac = Select(self.driver.find_element(By.ID, Locatorsolicitud.dp_entidad))
        select_entidad_nac.select_by_visible_text(entidadnac)

    def enter_curp(self, _curp):
        self.driver.find_element(By.ID, Locatorsolicitud.dp_curp).click()
        self.driver.find_element(By.ID, Locatorsolicitud.dp_curp).send_keys(Keys.RIGHT)
        self.driver.find_element(By.ID, Locatorsolicitud.dp_curp).send_keys(Keys.RIGHT)
        self.driver.find_element(By.ID, Locatorsolicitud.dp_curp).send_keys(_curp)
