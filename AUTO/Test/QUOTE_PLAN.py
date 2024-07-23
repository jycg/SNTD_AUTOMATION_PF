import time
import sys
import os
import logging
import traceback
from datetime import datetime
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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


def cotizador_plan_financiero(self, driver, fila):
    quote = QuotePage(driver)
    try:
        quote.click_plan(fila["var_plan"])
        time.sleep(9)

        print("\033[1;32m-" * 1 + " PLAN FINANCIERO EXITOSO " + "-\033[0m" * 1)

        if fila["var_accesorios"] == "SI":
            accesorios_select = quote.driver.find_element(By.ID, Locators.plan_accesorios)
            if accesorios_select.is_enabled():
                quote.click_accesorios("Accesorios Vehículo")
                quote.click_descripcion_accesorios("GPS")
                quote.click_monto_accesorios(fila["var_monto_accesorios"])
                if fila["var_producto_finan"] == "ARRENDAMIENTO":
                    pass
                else:
                    quote.click_accesorios_type(fila["var_forma_pago_acce"])
            else:
                print("El elemento de accesorios está deshabilitado.")
        else:
            pass

        element_g_ex = driver.find_element(By.ID, Locators.plan_g_ext)

        # Garantía Extendida
        if element_g_ex.is_enabled():
            if fila["var_g_ext"] == "SI":
                quote.click_garantia()
                time.sleep(1)
                quote.click_garantia_select()
                quote.click_monto_garantia(fila["var_monto_g_ext"])
                if fila["var_producto_finan"] == "ARRENDAMIENTO":
                    pass
                else:
                    quote.click_garantia_type(fila["var_forma_pago_g_ext"])
            else:
                pass
        else:
            pass

        time.sleep(5)
        quote.click_cuotas_show()
        time.sleep(3)
        print("\033[1;32m-" * 1 + " ACCESORIO EXITOSO Y GARANTÍA EXTENDIDA" + "-\033[0m" * 1)

        # Selección de plazos
        cuota_ = "{}{}".format("divTermContent_", fila["var_plazo"])
        str_monto = str(cuota_)
        try:
            element_plazo = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, str_monto))
            )
            element_plazo.click()
        except TimeoutException:
            commentplazo = "El plazo deseado no se encuentra visible. Verifica la configuración a detalle"
            logging.error(commentplazo)

        time.sleep(2)
        print("\033[1;32m-" * 1 + " CUOTAS EXITOSO " + "-\033[0m" * 1)

        # Si hay configuración de Garantía extendida en el plan financiero, entrará a seleccionar todas las opciones de Coberturas Adicionales
        if element_g_ex.is_enabled():
            pass
        else:
            if fila["var_g_ext"] == "SI":
                try:
                    quote.click_GE()
                except NoSuchElementException:
                    self.commentge = "Estás tratando de seleccionar garantía extendida pero no está configurado en el plan financiero"
                    print(f"Estás tratando de seleccionar garantía extendida pero no está configurado en el plan financiero. O bien, se tuvo un problema")
            else:
                pass

            if fila["var_seguro_robo_aut"] == "SI":
                try:
                    if fila["var_seguro_robo_aut_cobertura"] == "Advanced":
                        quote.click_SRA_Advanced()
                    elif fila["var_seguro_robo_aut_cobertura"] == "Signature":
                        quote.click_SRA_Signature()
                    else:
                        pass
                except NoSuchElementException:
                    self.commentrsa = "Estás tratando de seleccionar seguro de robo autopartes pero no está configurado en el plan financiero"
                    print(f"Estás tratando de seleccionar seguro de robo autopartes pero no está configurado en el plan financiero. O bien, se tuvo un problema")
            else:
                quote.click_label()

            if fila["var_gap"] == "SI":
                try:
                    element_gap_formapago = driver.find_element(By.ID, Locators.plan_seguro_gap_forma_pago)
                    if element_gap_formapago.is_enabled():
                        select_gap_formapago = Select(element_gap_formapago)

                        options = [option.text for option in select_gap_formapago.options]

                        if fila["var_gap_forma_pago"] in options:
                            quote.click_GaP_type(fila["var_gap_forma_pago"])
                            quote.click_GaP()
                        else:
                            print(f"La opción {fila['var_gap_forma_pago']} no está disponible en las opciones del select.")
                            pass
                    else:
                        print("El elemento plan_seguro_gap_forma_pago está deshabilitado.")
                        pass
                except NoSuchElementException:
                    print(f"Estás tratando de seleccionar seguro GaP pero no está configurado en el plan financiero. O bien, se tuvo un problema")

            else:
                quote.click_label()

            time.sleep(2)
            quote.click_aceptar_msj_gap()
            driver.execute_script('window.scrollBy(0, 500);')
            print("\033[1;32m-" * 1 + " COBERTURAS ADICIONALES EXITOSO " + "-\033[0m" * 1)

    except TimeoutException as e:
        error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
        if 'Message: Could not locate element with visible text' in error_message:
            print("Falló al seleccionar el plan financiero")
        logging.error(error_message)
        traceback.print_exc()
