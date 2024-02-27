import time
import sys
import os
import logging
import traceback
from datetime import datetime
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from AUTO.PageApp.quotePage import QuotePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


def cotizador_seguro_de_auto(driver, fila):
    quote = QuotePage(driver)
    try:
        # Obtiene la fecha del excel y lo convierte a formato "fecha"
        fecha_excel = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(fila["var_fecha"]) - 2)

        # Sección de seguro de daños
        if fila["var_seguro_danos"] == "PRIMA MANUAL":
            quote.click_insurance_manual()
        elif fila["var_seguro_danos"] == "NO":
            quote.click_insurance_no()
            time.sleep(2)
            quote.click_msj_aceptar()
            print("\033[1;32m-" * 1 + " SIN SEGURO DE DAÑO EXITOSO " + "-\033[0m" * 1)
        else:
            pass

        time.sleep(3)
        if fila["var_seguro_danos"] == "SI" or fila["var_seguro_danos"] == "PRIMA MANUAL":
            quote.click_insurance_cp()
            quote.clear_insurance_cp()
            quote.enter_insurance_cp(fila["var_cp"])
            if fila["var_producto_finan"] == "ARRENDAMIENTO":
                pass
            else:
                quote.click_insurance_formapago()
                quote.enter_insurance_formapago(fila["var_forma_pago"])
                time.sleep(2)
                quote.click_insurance_div()
                time.sleep(1)
                quote.click_insurance_tipo()
                quote.enter_insurance_tipo(fila["var_tipo"])
                time.sleep(2)
            quote.click_insurance_cobertura()
            quote.enter_insurance_cobertura(fila["var_cobertura"])
            time.sleep(1)
            quote.click_insurance_birthdate()
            quote.clear_insurance_birthdate()
            quote.enter_insurance_birthdate(fecha_excel.strftime('%d/%m/%Y'))
            time.sleep(1)
            quote.click_insurance_div()
            time.sleep(2)

            divautocompara = driver.find_element(By.ID, Locators.insurance_divautocompara)
            if "style" in divautocompara.get_attribute("outerHTML"):
                style_value = divautocompara.get_attribute("style")
                if style_value.strip() == "":
                    if fila["var_autocompara"] == "SI":
                        quote.click_insurance_autocompara_si()
                    else:
                        quote.click_insurance_autocompara_no()
                else:
                    pass

            if fila["var_sexo"] == "HOMBRE":
                quote.click_insurance_male()
            else:
                quote.click_insurance_female()

            element_udi = driver.find_element(By.ID, Locators.insurance_UDI)

            if element_udi.is_displayed():
                quote.select_insurance_UDI(fila["var_UDI"])
            else:
                pass

            if fila["var_seguro_danos"] == "PRIMA MANUAL":
                quote.select_insurance_agencia(fila["var_aseguradora"])
                quote.click_insurance_recibo1()
                quote.control_insurance_recibo1()
                quote.clear_insurance_recibo1()
                quote.enter_insurance_recibo1(fila["var_recibo1"])
                if fila["var_tipo"] == "MULTIANUAL FRACCIONADO":
                    quote.click_insurance_recibo2()
                    quote.control_insurance_recibo2()
                    quote.clear_insurance_recibo2()
                    quote.enter_insurance_recibo2(fila["var_recibo2"])
                    if fila["var_forma_pago"] == "Contado":
                        quote.enter_insurance_subsecuente(fila["var_subsecuente"])
            else:
                pass

            time.sleep(4)
            quote.click_insurance_msj_quote()
            time.sleep(10)

            if fila["var_seguro_danos"] == "SI":
                wait = WebDriverWait(driver, 60)
                locator_insurance = (By.XPATH, Locators.insurance_insurance)
                element_insurance = wait.until(EC.visibility_of_element_located(locator_insurance))
                element_insurance.click()
                time.sleep(10)
                print("\033[1;32m-" * 1 + " SEGURO DE AUTO EXITOSO " + "-\033[0m" * 1)
            else:
                pass
            time.sleep(3)
        else:
            pass

        time.sleep(2)
    except TimeoutException as e:
        error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
        logging.error(error_message)
        traceback.print_exc()
