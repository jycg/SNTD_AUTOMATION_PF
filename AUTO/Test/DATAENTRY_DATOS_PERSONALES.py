import time
import sys
import os
import logging
import traceback
import random
from datetime import datetime
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from AUTO.PageApp.quotePage import QuotePage
from AUTO.PageApp.solicitudPage import SolicitudPage
from faker import Faker
from AUTO.Locator.locators import Locators

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
fake = Faker()
log_dir = 'C:/Automation_Performance_Sast/app_log'
os.makedirs(log_dir, exist_ok=True)
log_subdir = datetime.now().strftime('%Y-%m-%d')
log_dir = os.path.join(log_dir, log_subdir)
os.makedirs(log_dir, exist_ok=True)
log_filename = os.path.join(log_dir, 'log.txt')
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def solicita_credito(driver, fila):
    try:
        quote = QuotePage(driver)
        if fila["var_crearsolicitud"] == "NO":
            pass
        else:
            # SOLICITA CRÉDITO
            quote.click_solicita_credito()
            time.sleep(1)
            quote.click_si_confirm()
            element_code = driver.find_element(By.XPATH, Locators.quote_divCodigoVerTemp)
            element_code_text = driver.execute_script('return arguments[0].innerText;', element_code)
            time.sleep(1)
            quote.codigo_verificacion(element_code_text)
            time.sleep(1)
            quote.click_btnGotoCreditform()
            time.sleep(5)

            solicitud_datos_personales(driver, fila)
    except TimeoutException as e:
        error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
        logging.error(error_message)
        traceback.print_exc()


def solicitud_datos_personales(driver, fila):
    try:
        solicitud = SolicitudPage(driver)
        print("\033[1;32m-" * 30 + " START SOLICITUD" + "-\033[0m" * 30)
        if fila["var_clienteSNTD"] == "SI":
            solicitud.click_client_sntd()
            random_buc = random.randint(00000000, 99999999)
            solicitud.enter_buc(random_buc)
        else:
            pass

        if fila["var_sexo_solicitud"] == "HOMBRE":
            solicitud.click_sexo_hombre()
        else:
            solicitud.click_sexo_mujer()

        fecha_solicitud = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(fila["var_fechanac"]) - 2)
        solicitud.enter_fecha(fecha_solicitud.strftime('%d/%m/%Y'))

        time.sleep(1)
        txtCURP = driver.find_element(By.ID, 'txtCURP').text
        txtCURP_ = txtCURP + " 02"
        solicitud.click_entidad_nac(fila["var_entidad"])
        time.sleep(2)
        solicitud.enter_curp(txtCURP_)
        time.sleep(2)
        solicitud.enter_homoclave(fila["var_homoclave"])

        #

        time.sleep(20)
    except TimeoutException as e:
        error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
        logging.error(error_message)
        traceback.print_exc()
