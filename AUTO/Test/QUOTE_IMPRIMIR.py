import re
import time
import unittest
import sys
import os
import xlrd
import logging
import traceback
import random
import string
from datetime import datetime
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from AUTO.PageApp.loginPage import LoginPage
from AUTO.PageApp.searchPage import SearchPage
from AUTO.PageApp.quotePage import QuotePage
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from AUTO.Locator.locators import Locators
from selenium.webdriver.edge.options import Options
from DATAENTRY_DATOS_PERSONALES import solicita_credito, solicitud_datos_personales
from QUOTE_PRODUCTO import cotizador_producto
from QUOTE_PLAN import cotizador_plan_financiero
from QUOTE_SEGURO import cotizador_seguro_de_auto
from QUOTE_DETALLE_FINANCIAMIENTO import cotizador_detalle_financiamiento
from QUOTE_DATOS_SOLICITANTE import cotizador_datos_solicitante

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