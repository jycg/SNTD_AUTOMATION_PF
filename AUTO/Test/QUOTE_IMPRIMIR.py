import time
import sys
import os
import logging
import traceback
from datetime import datetime
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from AUTO.PageApp.quotePage import QuotePage
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


def cotizador_imprimir(driver, fila):
    quote = QuotePage(driver)
    try:
        quote.click_imprimir()
        time.sleep(1)
        element_msj = driver.find_element(By.XPATH, Locators.alert_label)
        if element_msj.is_displayed():
            quote.click_aceptar_msj_gap()
        else:
            pass
    except TimeoutException as e:
        error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
        logging.error(error_message)
        traceback.print_exc()
