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

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
fake = Faker()
log_dir = 'C:/Automation_Performance_Sast/app_log'
os.makedirs(log_dir, exist_ok=True)
log_subdir = datetime.now().strftime('%Y-%m-%d')
log_dir = os.path.join(log_dir, log_subdir)
os.makedirs(log_dir, exist_ok=True)
log_filename = os.path.join(log_dir, 'log.txt')
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def cotizador_datos_solicitante(self, driver, fila):
    quote = QuotePage(driver)
    try:
        # Sección DATOS DEL SOLICITANTE
        if fila["var_faker"] == "SI":
            fname = fake.first_name()
            sname = fake.first_name()
            flastname = fake.last_name()
            slastname = fake.last_name()
        else:
            fname = "JULIO"
            sname = "DE JESÚS"
            flastname = "GARCÍA"
            slastname = "HERNÁNDEZ"

        quote.enter_fname(fname)
        quote.enter_sname(sname)
        quote.enter_flastname(flastname)
        quote.enter_slastname(slastname)
        self.namecomplete = ' '.join([fname, sname, flastname, slastname])
        quote.enter_lada(fila["lada"])
        quote.enter_phone(fila["telefono"])
        quote.enter_cellphone(fila["celular"])
        quote.click_cellcompany(fila["compania"])
        quote.enter_email(fila["email"])
        time.sleep(1)
    except TimeoutException as e:
        error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
        logging.error(error_message)
        traceback.print_exc()
