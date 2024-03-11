from AUTO.Locator.locators_solicitud import Locatorsolicitud
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SolicitudPage:
    def __init__(self, driver):
        self.driver = driver

    def click_client_sntd(self):
        try:
            client_sntd = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locatorsolicitud.dp_clientesntd))
            )
            client_sntd.click()
        except Exception as e:
            print(f"Error al hacer clic en cliente SNTD: {e}")

    def enter_buc(self, sntdbuc):
        try:
            buc_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, Locatorsolicitud.dp_txtBUC))
            )
            buc_input.send_keys(sntdbuc, Keys.ENTER)
        except Exception as e:
            print(f"Error al ingresar BUC: {e}")

    def click_sexo_hombre(self):
        try:
            sexo_hombre = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locatorsolicitud.dp_hombre))
            )
            sexo_hombre.click()
        except Exception as e:
            print(f"Error al hacer clic en sexo Hombre: {e}")

    def click_sexo_mujer(self):
        try:
            sexo_mujer = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locatorsolicitud.dp_mujer))
            )
            sexo_mujer.click()
        except Exception as e:
            print(f"Error al hacer clic en sexo Mujer: {e}")

    def enter_fecha(self, birthday):
        try:
            fecha_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, Locatorsolicitud.dp_fecha))
            )
            fecha_input.click()
            fecha_input.send_keys(Keys.CONTROL + "A")
            fecha_input.send_keys(Keys.CLEAR)
            fecha_input.send_keys(birthday)
        except Exception as e:
            print(f"Error al ingresar fecha de nacimiento: {e}")

    def click_entidad_nac(self, entidadnac):
        try:
            entidad_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, Locatorsolicitud.dp_entidad))
            )
            select_entidad_nac = Select(entidad_select)
            select_entidad_nac.select_by_visible_text(entidadnac)
        except Exception as e:
            print(f"Error al seleccionar entidad de nacimiento: {e}")

    def enter_curp(self, _curp):
        try:
            curp_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, Locatorsolicitud.dp_curp))
            )
            curp_input.click()
            curp_input.send_keys(Keys.RIGHT)
            curp_input.send_keys(Keys.RIGHT)
            curp_input.send_keys(_curp)
        except Exception as e:
            print(f"Error al ingresar CURP: {e}")

    def enter_homoclave(self, _homoclave):
        try:
            homoclave_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, Locatorsolicitud.dp_homoclave))
            )
            homoclave_input.click()
            homoclave_input.clear()
            homoclave_input.send_keys(_homoclave)
            time.sleep(1)
        except Exception as e:
            print(f"Error al ingresar homoclave: {e}")

    def select_edo_civil(self, edo_civil):
        try:
            edo_civil_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, Locatorsolicitud.dp_edocivil))
            )
            _edo_civil_select = Select(edo_civil_select)
            _edo_civil_select.select_by_visible_text(edo_civil)
        except Exception as e:
            print(f"Error al ingresar homoclave: {e}")

    def enter_dependientes(self, dependientes):
        self.driver.find_element(By.ID, Locatorsolicitud.dp_dependientes).send_keys(dependientes)

    def select_nivel_estudios(self, nivel_estudios):
        try:
            nivel_estudio_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, Locatorsolicitud.dp_nivelestudios))
            )
            _nivel_estudio_select = Select(nivel_estudio_select)
            _nivel_estudio_select.select_by_visible_text(nivel_estudios)
        except Exception as e:
            print(f"Error al ingresar homoclave: {e}")

    def select_ocupacion(self, ocupacion):
        try:
            ocupacion_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, Locatorsolicitud.dp_ocupacion))
            )
            _ocupacion_select = Select(ocupacion_select)
            _ocupacion_select.select_by_visible_text(ocupacion)
        except Exception as e:
            print(f"Error al ingresar homoclave: {e}")

    def enter_cp(self, zipcode):
        try:
            zipcode_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, Locatorsolicitud.dp_ZipCode))
            )
            zipcode_input.click()
            zipcode_input.send_keys(Keys.CONTROL + "A")
            zipcode_input.send_keys(Keys.CLEAR)
            zipcode_input.send_keys(zipcode)
        except Exception as e:
            print(f"Error al ingresar homoclave: {e}")

    def click_label(self):
        self.driver.find_element(By.XPATH, Locatorsolicitud.label_domicilio).click()

    def enter_colonia(self):
        try:
            colonia_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, Locatorsolicitud.dp_drpSuburb))
            )
            colonia_select.click()
            colonia_select.send_keys(Keys.DOWN)
            colonia_select.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Error al ingresar homoclave: {e}")

    def enter_calle(self, calle):
        try:
            zipcode_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, Locatorsolicitud.dp_txtStreet))
            )
            zipcode_input.click()
            zipcode_input.send_keys(Keys.CONTROL + "A")
            zipcode_input.send_keys(Keys.CLEAR)
            zipcode_input.send_keys(calle)
        except Exception as e:
            print(f"Error al ingresar homoclave: {e}")
