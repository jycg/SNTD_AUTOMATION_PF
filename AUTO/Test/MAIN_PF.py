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
from QUOTE_IMPRIMIR import cotizador_imprimir
from LOG import cotizador_log

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
fake = Faker()
log_dir = 'C:/Automation_Performance_Sast/app_log'
os.makedirs(log_dir, exist_ok=True)
log_subdir = datetime.now().strftime('%Y-%m-%d')
log_dir = os.path.join(log_dir, log_subdir)
os.makedirs(log_dir, exist_ok=True)
log_filename = os.path.join(log_dir, 'log.txt')
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class MyTestCase(unittest.TestCase):
    driver = None

    def __init__(self, *args, **kwargs):
        super(MyTestCase, self).__init__(*args, **kwargs)
        self.final_string = ""
        self.commentgap = ""
        self.commentrsa = ""
        self.commentge = ""
        self.ballon_and_tcm = ''
        self.TblamortizationTCM = ''
        self.namecomplete = ''
        self.productall = ''
        self.lblcar = ''
        self.lblpricelist = ''
        self.tdaccessoriesamount = ''
        self.tdadditionalcoverageamount = ''
        self.tdextendedwarrantyamount = ''
        self.tdautopartstheftinsuranceamount = ''
        self.tdInsuranceGAPAmount = ''
        self.tdTasa = ''
        self.tdPLazo = ''
        self.lblSeguroVd = ''
        self.tdSeguro = ''
        self.replace_divInsuranceRecipes = ''
        self.lblEnganche = ''
        self.tasaC2 = ''
        self.plazoC2 = ''
        self.tdComision = ''
        self.tdDesembolso = ''
        self.tdFinanciar = ''
        self.tdMensualidad = ''
        self.cat = ''
        self.cuotasall = ''
        self.Tblamortization = ''

    @classmethod
    def setUpClass(cls):
        s = "C:/Users/jgarcia/PycharmProjects/SNTDProject/drivers/Edge/121/msedgedriver.exe"
        edge_service = EdgeService(s)
        edge_options = Options()
        edge_options.add_argument('--ignore-certificate-errors')
        edge_options.add_argument('--ignore-ssl-errors')
        cls.driver = webdriver.Edge(service=edge_service, options=edge_options)
        cls.driver.delete_all_cookies()
        if "data:" not in cls.driver.current_url:
            cls.driver.execute_script("localStorage.clear();")
            cls.driver.execute_script("sessionStorage.clear();")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_cotizador_valid(self):
        archivo_excel = xlrd.open_workbook('C:/Automation_Performance_Sast/SNTD_QUOTE_PF_TEST.xls')
        sheet_environment = archivo_excel.sheet_by_index(0)
        fila_environment = {
            "var_environment": sheet_environment.cell_value(1, 0),
            "var_url": sheet_environment.cell_value(1, 1),
            "var_canal": sheet_environment.cell_value(1, 2),
            "var_user": sheet_environment.cell_value(1, 3)
        }
        print(fila_environment)
        sheet_quote = archivo_excel.sheet_by_index(1)
        for numero_fila in range(1, sheet_quote.nrows):
            fila = {
                "var_escenario": int(sheet_quote.cell_value(numero_fila, 0)),
                "var_agencia": sheet_quote.cell_value(numero_fila, 1),
                "var_tipo_credito": sheet_quote.cell_value(numero_fila, 2),
                "var_producto_finan": sheet_quote.cell_value(numero_fila, 3),
                "var_tipo_producto": sheet_quote.cell_value(numero_fila, 4),
                "var_tipo_uso": sheet_quote.cell_value(numero_fila, 5),
                "var_tipo_persona": sheet_quote.cell_value(numero_fila, 6),
                "var_marca": sheet_quote.cell_value(numero_fila, 7),
                "var_modelo": sheet_quote.cell_value(numero_fila, 8),
                "var_version": sheet_quote.cell_value(numero_fila, 9),
                "var_ano": int(sheet_quote.cell_value(numero_fila, 10)),
                "var_plan": sheet_quote.cell_value(numero_fila, 11),
                "var_accesorios": sheet_quote.cell_value(numero_fila, 12),
                "var_monto_accesorios": sheet_quote.cell_value(numero_fila, 13),
                "var_forma_pago_acce": sheet_quote.cell_value(numero_fila, 14),
                "var_g_ext": sheet_quote.cell_value(numero_fila, 15),
                "var_monto_g_ext": sheet_quote.cell_value(numero_fila, 16),
                "var_forma_pago_g_ext": sheet_quote.cell_value(numero_fila, 17),
                "var_plazo": int(sheet_quote.cell_value(numero_fila, 18)),
                "var_seguro_robo_aut": sheet_quote.cell_value(numero_fila, 19),
                "var_gap": sheet_quote.cell_value(numero_fila, 20),
                "var_seguro_danos": sheet_quote.cell_value(numero_fila, 21),
                "var_forma_pago": sheet_quote.cell_value(numero_fila, 22),
                "var_tipo": sheet_quote.cell_value(numero_fila, 23),
                "var_cp": sheet_quote.cell_value(numero_fila, 24),
                "var_cobertura": sheet_quote.cell_value(numero_fila, 25),
                "var_fecha": sheet_quote.cell_value(numero_fila, 26),
                "var_sexo": sheet_quote.cell_value(numero_fila, 27),
                "var_UDI": sheet_quote.cell_value(numero_fila, 28),
                "var_recibo1": sheet_quote.cell_value(numero_fila, 29),
                "var_recibo2": sheet_quote.cell_value(numero_fila, 30),
                "var_subsecuente": sheet_quote.cell_value(numero_fila, 31),
                "var_autocompara": sheet_quote.cell_value(numero_fila, 32),
                "var_aseguradora": sheet_quote.cell_value(numero_fila, 33),
                "var_faker": sheet_quote.cell_value(numero_fila, 34),
                "lada": sheet_quote.cell_value(numero_fila, 35),
                "telefono": sheet_quote.cell_value(numero_fila, 36),
                "celular": sheet_quote.cell_value(numero_fila, 37),
                "compania": sheet_quote.cell_value(numero_fila, 38),
                "email": sheet_quote.cell_value(numero_fila, 39),
                "var_tbl_amortiza": sheet_quote.cell_value(numero_fila, 40),
                "var_crearsolicitud": sheet_quote.cell_value(numero_fila, 41),
                "var_clienteSNTD": sheet_quote.cell_value(numero_fila, 42),
                "var_sexo_solicitud": sheet_quote.cell_value(numero_fila, 43),
                "var_fechanac": sheet_quote.cell_value(numero_fila, 44),
                "var_entidad": sheet_quote.cell_value(numero_fila, 45),
                "var_homoclave": sheet_quote.cell_value(numero_fila, 46),
                "var_curp": sheet_quote.cell_value(numero_fila, 47),
                "var_edocivil": sheet_quote.cell_value(numero_fila, 48),
                "var_r_matrimonial": sheet_quote.cell_value(numero_fila, 49),
                "var_dependientes": sheet_quote.cell_value(numero_fila, 50),
                "var_nivelestudio": sheet_quote.cell_value(numero_fila, 51),
                "var_ocupacion": sheet_quote.cell_value(numero_fila, 52),
            }
            print(fila)
            try:
                self.login(fila, fila_environment)
                self.cotizador_producto(fila, fila_environment)
                self.cotizador_plan_financiero(fila)
                self.cotizador_seguro_de_auto(fila)
                self.cotizador_detalle_financiamiento(fila)
                self.cotizador_datos_solicitante(fila)
                self.cotizador_imprimir(fila)
                self.cotizador_log(fila)
                self.solicita_credito(fila)
                # self.solicitud_datos_personales(fila)
            except Exception as e:
                error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
                logging.error(error_message)
                print(error_message)
                # traceback.print_exc()

    def login(self, fila, fila_environment):
        try:
            driver = self.driver
            login = LoginPage(driver)
            search = SearchPage(driver)
            quote = QuotePage(driver)
            print("                                                                    ")
            print("\033[1;32m*" * 30 + " ESCENARIO # ", fila["var_escenario"], "*\033[0m" * 30)
            if fila_environment["var_environment"] == "BYD_QA":
                if fila["var_producto_finan"] == "ARRENDAMIENTO" or fila["var_tipo_uso"] == "CHOFER PRVADO" or fila["var_tipo_uso"] == "COMERCIAL" or \
                        fila["var_tipo_producto"] == "SEMINUEVO" or fila["var_tipo_producto"] == "MOTO" or fila["var_marca"] != "BYD":
                    print("La configuración no forma parte del proyecto, revisa los datos e intenta de nuevo")
                    self.driver.quit()
            else:
                pass
            driver.get(fila_environment["var_url"])

            # LOGIN
            if fila_environment["var_environment"] != "BYD_QA" and fila_environment["var_environment"] != "OM2":
                login.enter_username(fila_environment["var_user"])
                login.enter_password("S1santan")
                login.click_login()
                print("\033[1;32m-" * 1 + " LOGIN EXITOSO " + "-\033[0m" * 1)

                # Búsqueda de Cotizaciones
                search.click_nvaCot()
                print("\033[1;32m-" * 1 + " BÚSQUEDA EXITOSA " + "-\033[0m" * 1)

                # NVA COTIZACIÓN
                time.sleep(2)
                quote.click_agencia()
                quote.enter_agencia(fila["var_agencia"])
            else:
                pass
        except TimeoutException as e:
            error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
            logging.error(error_message)
            traceback.print_exc()

    def cotizador_producto(self, fila, fila_environment):
        cotizador_producto(self.driver, fila, fila_environment)

    def cotizador_plan_financiero(self, fila):
        cotizador_plan_financiero(self, self.driver, fila)

    def cotizador_seguro_de_auto(self, fila):
        cotizador_seguro_de_auto(self.driver, fila)

    def cotizador_detalle_financiamiento(self, fila):
        cotizador_detalle_financiamiento(self, self.driver, fila)

    def cotizador_datos_solicitante(self, fila):
        cotizador_datos_solicitante(self, self.driver, fila)

    def cotizador_imprimir(self, fila):
        cotizador_imprimir(self.driver, fila)

    def cotizador_log(self, fila):
        try:
            driver = self.driver
            driver.save_screenshot('screenshotsssssss.png')
            print("\033[1;32m-" * 1 + " DATOS DEL SOLICITANTE EXITOSO " + "-\033[0m" * 1)
            comments_all = "GAP: {}, SRA: {}, GE: {}".format(self.commentgap, self.commentrsa, self.commentge)
            # Guarda información en el log
            logging.info("*" * 45 + " ESCENARIO: %s " + "*" * 45 + "\n"
                                                                   "- [Nombre Cliente]: %s\n"
                                                                   "- [PRODUCTO]: %s\n"
                                                                   "- [Vehículo]: %s\n"
                                                                   "- [Valor del Vehículo]: %s\n"
                                                                   "- [Accesorios Vehículo]: %s\n"
                                                                   "- [Coberturas Adicionales]: %s\n"
                                                                   "- [Garantía Extendida]: %s\n"
                                                                   "- [Seguro de Robo de Autopartes]: %s\n"
                                                                   "- [Seguro GAP]: %s\n"
                                                                   "- [Tasa Fija]: %s\n"
                                                                   "- [Plazo]: %s\n"
                                                                   "- [Seguro de Vida y Desempleo]: %s\n"
                                                                   "- [Seguro del vehículo Año 1]: %s\n"
                                                                   "- [Subsecuente]: %s\n"
                                                                   "- [Enganche]: %s\n"
                                                                   f"- [{self.ballon_and_tcm}] %s\n"
                                                                   "- [Tasa Fija Ciclo 2]: %s\n"
                                                                   "- [Plazo Ciclo 2]: %s\n"
                                                                   "- [Comisión Apertura]: %s\n"
                                                                   "- [Desembolso Inicial]: %s\n"
                                                                   "- [Monto a Financiar]: %s\n"
                                                                   "- [Primer Pago]: %s\n"
                                                                   "- [CAT]: %s\n"
                                                                   "- [Cuotas All]: %s\n"
                                                                   "- [Tabla de Amortización]: %s\n"
                                                                   f"- [{self.TblamortizationTCM}] %s\n"
                                                                   "- [Comentarios generales]: %s\n",
                         fila["var_escenario"], self.namecomplete, self.productall, self.lblcar, self.lblpricelist, self.tdaccessoriesamount, self.tdadditionalcoverageamount,
                         self.tdextendedwarrantyamount, self.tdautopartstheftinsuranceamount, self.tdInsuranceGAPAmount, self.tdTasa, self.tdPLazo, self.lblSeguroVd, self.tdSeguro,
                         self.replace_divInsuranceRecipes, self.lblEnganche, '', self.tasaC2, self.plazoC2, self.tdComision, self.tdDesembolso, self.tdFinanciar, self.tdMensualidad, self.cat,
                         self.cuotasall, self.Tblamortization, '', comments_all)

            print("\033[1;32m-" * 1 + " FINISHED COTIZACIÓN" + "-\033[0m" * 1)
            time.sleep(10)
        except TimeoutException as e:
            error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
            logging.error(error_message)
            traceback.print_exc()

    # def solicita_credito(self, fila):
    #     driver = self.driver
    #     quote = QuotePage(driver)
    #     try:
    #         if fila["var_crearsolicitud"] == "NO":
    #             pass
    #         else:
    #             # SOLICITA CRÉDITO
    #             quote.click_solicita_credito()
    #             time.sleep(1)
    #             quote.click_si_confirm()
    #             element_code = driver.find_element(By.XPATH, Locators.quote_divCodigoVerTemp)
    #             element_code_text = driver.execute_script('return arguments[0].innerText;', element_code)
    #             time.sleep(1)
    #             quote.codigo_verificacion(element_code_text)
    #             time.sleep(1)
    #             quote.click_btnGotoCreditform()
    #             time.sleep(5)
    #
    #             self.solicitud_datos_personales(fila)
    #     except TimeoutException as e:
    #         error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
    #         logging.error(error_message)
    #         traceback.print_exc()
    #
    # def solicitud_datos_personales(self, fila):
    #     driver = self.driver
    #     solicitud = SolicitudPage(driver)
    #     try:
    #         print("\033[1;32m-" * 30 + " START SOLICITUD" + "-\033[0m" * 30)
    #         if fila["var_clienteSNTD"] == "SI":
    #             solicitud.click_client_sntd()
    #             random_buc = random.randint(00000000, 99999999)
    #             solicitud.enter_buc(random_buc)
    #         else:
    #             pass
    #
    #         if fila["var_sexo_solicitud"] == "HOMBRE":
    #             solicitud.click_sexo_hombre()
    #         else:
    #             solicitud.click_sexo_mujer()
    #
    #         fecha_solicitud = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(fila["var_fechanac"]) - 2)
    #         solicitud.enter_fecha(fecha_solicitud.strftime('%d/%m/%Y'))
    #
    #         time.sleep(1)
    #         self.txtCURP = self.driver.find_element(By.ID, 'txtCURP').text
    #         txtCURP_ = self.txtCURP + " 02"
    #         solicitud.click_entidad_nac(fila["var_entidad"])
    #         time.sleep(2)
    #         solicitud.enter_curp(txtCURP_)
    #
    #         time.sleep(12)
    #     except TimeoutException as e:
    #         error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
    #         logging.error(error_message)
    #         traceback.print_exc()
    def solicita_credito(self, fila):
        solicita_credito(self.driver, fila)

    def solicitud_datos_personales(self, fila):
        solicitud_datos_personales(self.driver, fila)

    def tearDown(self):
        try:
            time.sleep(1)
            self.driver.quit()
            time.sleep(2)
        except Exception as e:
            error_message = f"Error en el escenario : {str(e)}"
            logging.error(error_message + "validando en el log")


if __name__ == '__main__':
    unittest.main()
