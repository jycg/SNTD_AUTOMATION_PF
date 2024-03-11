from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import unittest
from AUTO.PageApp.loginPage import LoginPage
from AUTO.PageApp.searchPage import SearchPage
from AUTO.PageApp.quotePage import QuotePage
from AUTO.Data.database import Database
import sys
import os
import xlrd
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import logging
import datetime
import traceback
from AUTO.Locator.locators import Locators

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
fake = Faker()
log_dir = 'C:/Automation_Performance_Sast/app_log'
os.makedirs(log_dir, exist_ok=True)
log_subdir = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_dir = os.path.join(log_dir, log_subdir)
os.makedirs(log_dir, exist_ok=True)
log_filename = os.path.join(log_dir, 'log.txt')
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class MyTestCase(unittest.TestCase):
    driver = None
    location_quote = "C:/Automation_Performance_Sast/SNTD_QUOTE_PF.xls"
    var_excel_quote = xlrd.open_workbook(location_quote)
    template_quote = var_excel_quote.sheet_by_index(0)

    @classmethod
    def setUpClass(cls):
        s = "C:/Users/jgarcia/PycharmProjects/SNTDProject/drivers/Edge/120/msedgedriver.exe"
        edge_service = EdgeService(s)
        cls.driver = webdriver.Edge(service=edge_service)
        cls.driver.delete_all_cookies()
        if "data:" not in cls.driver.current_url:
            cls.driver.execute_script("localStorage.clear();")
            cls.driver.execute_script("sessionStorage.clear();")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        # archivo_excel = xlrd.open_workbook('C:/Automation_Performance_Sast/SNTD_QUOTE_PF.xls')
        archivo_excel = xlrd.open_workbook('C:/Automation_Performance_Sast/SNTD_QUOTE_PF_TEST.xls')
        hoja = archivo_excel.sheet_by_index(0)
        for numero_fila in range(1, hoja.nrows):
            fila = {
                "var_escenario": int(hoja.cell_value(numero_fila, 0)),
                "var_ambiente": hoja.cell_value(numero_fila, 1),
                "var_canal": hoja.cell_value(numero_fila, 2),
                "var_agencia": hoja.cell_value(numero_fila, 3),
                "var_producto_finan": hoja.cell_value(numero_fila, 4),
                "var_tipo_producto": hoja.cell_value(numero_fila, 5),
                "var_tipo_uso": hoja.cell_value(numero_fila, 6),
                "var_tipo_persona": hoja.cell_value(numero_fila, 7),
                "var_plan": hoja.cell_value(numero_fila, 8),
                "var_accesorios": hoja.cell_value(numero_fila, 9),
                "var_monto_accesorios": hoja.cell_value(numero_fila, 10),
                "var_forma_pago_acce": hoja.cell_value(numero_fila, 11),
                "var_plazo": int(hoja.cell_value(numero_fila, 12)),
                "var_garantia_ext": hoja.cell_value(numero_fila, 13),
                "var_seguro_robo_aut": hoja.cell_value(numero_fila, 14),
                "var_gap": hoja.cell_value(numero_fila, 15),
                "var_seguro_danos": hoja.cell_value(numero_fila, 16),
                "var_forma_pago": hoja.cell_value(numero_fila, 17),
                "var_tipo": hoja.cell_value(numero_fila, 18),
                "var_cp": hoja.cell_value(numero_fila, 19),
                "var_cobertura": hoja.cell_value(numero_fila, 20),
                "var_fecha": hoja.cell_value(numero_fila, 21),
                "var_sexo": hoja.cell_value(numero_fila, 22),
                "var_recibo1": hoja.cell_value(numero_fila, 23),
                "var_recibo2": hoja.cell_value(numero_fila, 24),
                "var_subsecuente": hoja.cell_value(numero_fila, 25),
                "var_ejemplo": hoja.cell_value(numero_fila, 26),
                # Continúa con el resto de los valores
            }
            print(fila)
            try:
                self.realizar_acciones_con_fila(fila)
            except Exception as e:
                error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
                logging.error(error_message)
                print(error_message)
                traceback.print_exc()

    def realizar_acciones_con_fila(self, fila):
        try:
            database = Database()
            print("                                                                    ")
            print("                                                                    ")
            print("********************************** ESCENARIO # ", fila["var_escenario"],
                  "**********************************")
            driver = self.driver
            print(fila)
            driver.quit()
            driver.close()
            print("----------------- SECCIÓN LOGIN -----------------")
            if fila["var_ambiente"] == "TEST1":
                driver.get("https://sntdtest.tekprovider.net:9444/TekFinauto/Autogestion/Acceso/Login")
            elif fila["var_ambiente"] == "TEST2":
                driver.get("https://sntdqa.tekprovider.net:9081/TekFinauto/Autogestion/Acceso/Login")
            elif fila["var_ambiente"] == "UAT1":
                driver.get("http://192.168.30.225:83/TekFinauto/Autogestion/Acceso/Login")
            elif fila["var_ambiente"] == "UAT2":
                driver.get("http://192.168.30.225:92/TekFinauto/Autogestion/Acceso/Login")
            elif fila["var_ambiente"] == "PRE":
                driver.get("https://gcscreditoautobo.pre.mx.corp/TekFinauto/autogestion/Acceso/Login")
            elif fila["var_ambiente"] == "PROD":
                driver.get("https://www.autocredit-santander.com.mx/TekFinauto/AUTOGESTION/authentication")
            elif fila["var_ambiente"] == "DEV":
                driver.get("http://192.168.30.80:92/tekfinauto/autogestion/acceso/login")
            else:
                print("El ambiente no existe, verifica de nuevo la información")
                driver.close()
                driver.quit()

            login = LoginPage(driver)
            if fila["var_canal"] == "AGENCIA":
                login.enter_username("TBBT01")
            elif fila["var_canal"] == "SUCURSAL":
                login.enter_username("TBBT02")
            else:
                print("Error con el usuario. Verifica la configuración")
                driver.close()
                driver.quit()

            login.enter_password("S1santan")
            login.click_login()

            print("Sección LOGIN exitoso")
            # print("----------------- SECCIÓN BÚSQUEDA -----------------")
            search = SearchPage(driver)
            search.click_nvaCot()
            print("Sección BÚSQUEDA exitoso")

            print("----------------- SECCIÓN PRODUCTO -----------------")
            quote = QuotePage(driver)
            time.sleep(2)
            quote.click_agencia()
            quote.enter_agencia(fila["var_agencia"])

            if fila["var_producto_finan"] == "ARRENDAMIENTO":
                quote.click_arrendamiento()
            else:
                quote.click_credito()

            if fila["var_tipo_producto"] == "NUEVO":
                quote.click_tipon()
            elif fila["var_tipo_producto"] == "SEMINUEVO":
                quote.click_tipos()
            else:
                quote.click_tipom()

            if fila["var_canal"] == "AGENCIA":
                if fila["var_tipo_uso"] == "PARTICULAR":
                    quote.click_uso_p()
                elif fila["var_tipo_uso"] == "CHOFER PRVADO":
                    quote.click_uso_cp()
                else:
                    quote.click_uso_c()
            else:
                quote.click_uso_p()

            if fila["var_tipo_persona"] == "FISICA":
                quote.click_persona_f()
            else:
                quote.click_persona_fae()

            time.sleep(1)
            quote.click_marca()

            if fila["var_producto_finan"] == "CREDITO" and fila["var_tipo_producto"] == "NUEVO":
                quote.enter_marca("KIA")
                time.sleep(1)
                quote.click_modelo()
                quote.enter_modelo("FORTE")
                time.sleep(1)
                quote.click_version()
                quote.enter_version("1.6 GT DCT")
                time.sleep(1)
                quote.click_ano()
                quote.enter_ano_down1()
                time.sleep(1)
                quote.enter_ano()
            elif fila["var_producto_finan"] == "ARRENDAMIENTO" and fila["var_tipo_producto"] == "NUEVO":
                quote.enter_marca("TESLA")
                time.sleep(1)
                quote.click_modelo()
                quote.enter_modelo("MODEL 3")
                time.sleep(1)
                quote.click_version()
                quote.enter_version("AUTONOMIA MAYOR")
                time.sleep(1)
                quote.click_ano()
                quote.enter_ano_down1()
                time.sleep(1)
                quote.enter_ano()
            elif (fila["var_producto_finan"] == "CREDITO" or fila["var_producto_finan"] == "ARRENDAMIENTO") and fila[
                "var_tipo_producto"] == "SEMINUEVO":
                quote.enter_marca("ACURA")
                time.sleep(1)
                quote.click_modelo()
                quote.enter_modelo("INTEGRA")
                time.sleep(1)
                quote.click_version()
                quote.enter_version("A-SPEC")
                time.sleep(1)
                quote.click_ano()
                quote.enter_ano_down1()
                time.sleep(1)
                quote.enter_ano()
                quote.click_monto_vehiculo()
                time.sleep(1)
                quote.control_monto_vehiculo()
                time.sleep(1)
                quote.clear_monto_vehiculo()
                time.sleep(2)
                quote.enter_monto_vehiculo("$810,900.00")
            elif (fila["var_producto_finan"] == "CREDITO" or fila["var_producto_finan"] == "ARRENDAMIENTO") and fila[
                "var_tipo_producto"] == "MOTO":
                quote.enter_marca("KTM")
                time.sleep(1)
                quote.click_modelo()
                quote.enter_modelo("CROSS COUNTRY")
                time.sleep(1)
                quote.click_version()
                quote.enter_version("250 XC-F")
                time.sleep(1)
                quote.click_ano()
                quote.enter_ano_down1()
                time.sleep(1)
                quote.enter_ano()
            else:
                print("Ocurrió un error en las configuraiones del vehículo. Revisa tu set de datos predefinidos")

            print("Sección PRODUCTO exitoso")
            driver.find_element(By.ID, "divListPrice").click()
            time.sleep(3)

            print("---------- SECCIÓN PLAN DE FINANCIAMIENTO ----------")
            quote.click_plan(fila["var_plan"])
            time.sleep(9)
            print("Sección PLAN FINANCIERO exitoso")

            if fila["var_accesorios"] == "SI":
                accesorios_select = quote.driver.find_element(By.ID, Locators.plan_accesorios)
                if accesorios_select.is_enabled():
                    quote.click_accesorios("Accesorios Vehículo")
                    quote.click_descripcion_accesorios("GPS")
                    quote.click_monto_accesorios(fila["var_monto_accesorios"])
                    quote.click_accesorios_type(fila["var_forma_pago_acce"])
                else:
                    print("El elemento de accesorios está deshabilitado.")
            else:
                pass

            time.sleep(5)
            quote.click_cuotas_show()
            time.sleep(3)
            print("Sección ACCESORIO exitoso")

            cuota_ = "{}{}".format("divTermContent_", fila["var_plazo"])
            str_monto = str(cuota_)
            try:
                element_plazo = WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located((By.ID, str_monto))
                )
                element_plazo.click()
            except TimeoutException:
                print("El elemento 'element_plazo' no se encontró a tiempo.")
            time.sleep(2)
            print("Sección CUOTAS exitoso")

            if fila["var_garantia_ext"] == "SI":
                quote.click_GE()
            else:
                quote.click_label()

            if fila["var_seguro_robo_aut"] == "SI":
                quote.click_SRA()
            else:
                quote.click_label()

            if fila["var_gap"] == "SI":
                quote.click_GaP()
            else:
                quote.click_label()

            time.sleep(2)
            quote.click_aceptar_msj_gap()
            driver.execute_script('window.scrollBy(0, 500);')
            print("Sección COBERTURAS ADICIONALES exitoso")

            fecha_excel = datetime.datetime.fromordinal(
                datetime.datetime(1900, 1, 1).toordinal() + int(fila["var_fecha"]) - 2)
            # print(fecha_excel.strftime('%d/%m/%Y'))

            print("------------------ SEGURO DE AUTO ------------------")
            if fila["var_seguro_danos"] == "PRIMA MANUAL":
                quote.click_insurance_manual()
            elif fila["var_seguro_danos"] == "NO":
                quote.click_insurance_no()
                time.sleep(2)
                quote.click_msj_aceptar()
            else:
                pass

            time.sleep(3)
            if fila["var_seguro_danos"] == "SI" or fila["var_seguro_danos"] == "PRIMA MANUAL":
                quote.click_insurance_formapago()
                quote.enter_insurance_formapago(fila["var_forma_pago"])
                time.sleep(2)
                quote.click_insurance_div()
                time.sleep(1)
                quote.click_insurance_tipo()
                quote.enter_insurance_tipo(fila["var_tipo"])
                time.sleep(1)
                quote.click_insurance_cp()
                quote.clear_insurance_cp()
                quote.enter_insurance_cp(fila["var_cp"])
                time.sleep(2)
                quote.click_insurance_cobertura()
                quote.enter_insurance_cobertura(fila["var_cobertura"])
                time.sleep(1)
                quote.click_insurance_birthdate()
                quote.clear_insurance_birthdate()
                quote.enter_insurance_birthdate(fecha_excel.strftime('%d/%m/%Y'))
                time.sleep(1)
                quote.click_insurance_div()
                time.sleep(3)
                if fila["var_sexo"] == "HOMBRE":
                    quote.click_insurance_male()
                else:
                    quote.click_insurance_female()

                print("FORMA DE PAGO:", fila["var_forma_pago"])
                print("TIPO:", fila["var_tipo"])
                print("CÓDIGO POSTAL:", int(fila["var_cp"]))
                print("COBERTURA:", fila["var_cobertura"])

                if fila["var_seguro_danos"] == "PRIMA MANUAL":
                    quote.click_insurance_recibo1()
                    quote.control_insurance_recibo1()
                    quote.clear_insurance_recibo1()
                    quote.enter_insurance_recibo1(fila["var_recibo1"])
                    if fila["var_tipo"] == "Multianual fraccionado":
                        quote.click_insurance_recibo2()
                        quote.control_insurance_recibo2()
                        quote.clear_insurance_recibo2()
                        quote.enter_insurance_recibo2(fila["var_recibo2"])
                else:
                    pass
                time.sleep(4)
                quote.click_insurance_msj_quote()
                time.sleep(10)
                if fila["var_seguro_danos"] == "SI":
                    wait = WebDriverWait(driver, 30)
                    locator_insurance = (By.XPATH, Locators.insurance_insurance)
                    element_insurance = wait.until(EC.visibility_of_element_located(locator_insurance))
                    element_insurance.click()
                else:
                    pass
                time.sleep(3)
            else:
                pass
            time.sleep(12)
            print("Sección de SEGURO exitoso")

            print("------------------ DETALLE DE FINANCIAMIENTO ------------------")
            # Producto
            productall = "Prodcuto financiero: {}, Tipo de Producto: {}, Uso: {}, Tipo de Persona: {}".format(
                fila["var_producto_finan"], fila["var_tipo_producto"], fila["var_tipo_uso"], fila["var_tipo_persona"])
            # Cuota
            txtpay12: str = self.driver.find_element(By.XPATH, Locators.txtPay12).text
            txtpay24: str = self.driver.find_element(By.XPATH, Locators.txtPay24).text
            txtpay36: str = self.driver.find_element(By.XPATH, Locators.txtPay36).text
            txtpay48: str = self.driver.find_element(By.XPATH, Locators.txtPay48).text
            txtpay60: str = self.driver.find_element(By.XPATH, Locators.txtPay60).text
            txtpay72: str = self.driver.find_element(By.XPATH, Locators.txtPay72).text
            cuotasall = "Cuota 12: {}, Cuota 24: {}, Cuota 36: {}, Cuota 48: {}, Cuota 60: {}, Cuota 72: {}".format(
                txtpay12, txtpay24, txtpay36, txtpay48, txtpay60, txtpay72)
            # Vehículo
            lblcar: str = self.driver.find_element(By.ID, Locators.amortizationdetail_lblCar).text
            # Valor del Vehículo
            lblpricelist: str = self.driver.find_element(By.ID, Locators.amortizationdetail_lblPriceList).text
            # Accesorios Vehículo
            tdaccessories: str = self.driver.find_element(By.ID, 'tdAccessories').text
            tdaccessoriesamount: str = self.driver.find_element(By.ID, 'tdAccessoriesAmount').text
            # Coberturas Adicionales
            tdadditionalcoverage: str = self.driver.find_element(By.ID, 'tdAdditionalCoverage').text
            tdadditionalcoverageamount: str = self.driver.find_element(By.ID, 'tdAdditionalCoverageAmount').text
            # Garantía Extendida
            tdextendedwarranty: str = self.driver.find_element(By.ID, 'tdExtendedWarranty').text
            tdextendedwarrantyamount: str = self.driver.find_element(By.ID, 'tdExtendedWarrantyAmount').text
            # Seguro de Robo de Autopartes
            tdautopartstheftinsurance: str = self.driver.find_element(By.ID, 'tdAutoPartsTheftInsurance').text
            tdautopartstheftinsuranceamount: str = self.driver.find_element(By.ID,
                                                                            'tdAutoPartsTheftInsuranceAmount').text
            # Seguro GAP
            tdInsuranceGAP: str = self.driver.find_element(By.ID, 'tdInsuranceGAP').text
            tdInsuranceGAPAmount: str = self.driver.find_element(By.ID, 'tdInsuranceGAPAmount').text
            # Tasa Fija
            tdTasa: str = self.driver.find_element(By.ID, 'tdTasa').text
            # Plazo
            tdPLazo = self.driver.find_element(By.ID, 'tdPLazo').text
            # Seguro de Vida y Desempleo
            lblSeguroVd = self.driver.find_element(By.ID, 'lblSeguroVd').text
            # Seguro del vehículo Año 1
            thInsuranceDec = self.driver.find_element(By.ID, 'thInsuranceDec').text
            tdSeguro = self.driver.find_element(By.ID, 'tdSeguro').text
            divInsuranceRecipesHead = None
            divInsuranceRecipes = None

            if (fila["var_seguro_danos"] == "SI" or fila["var_seguro_danos"] == "SI") and fila[
                "var_tipo"] == "Multianual fraccionado":
                try:
                    # Intenta encontrar el elemento divInsuranceRecipesHead
                    divInsuranceRecipesHead = self.driver.find_element(By.ID, 'divInsuranceRecipesHead').text
                except NoSuchElementException:
                    divInsuranceRecipesHead = "No hay información disponible en divInsuranceRecipesHead"

                try:
                    # Intenta encontrar el elemento divInsuranceRecipes
                    divInsuranceRecipes = self.driver.find_element(By.ID, 'divInsuranceRecipes').text
                except NoSuchElementException:
                    divInsuranceRecipes = "No hay información disponible en divInsuranceRecipes"
            else:
                # Realiza alguna acción o manejo de excepciones en caso de que no se cumpla la condición
                pass
            # subsecuenteall = "{} {}".format(divInsuranceRecipesHead, divInsuranceRecipes)
            # Enganche
            captionDownpayment = self.driver.find_element(By.ID, 'captionDownpayment').text
            lblEnganche = self.driver.find_element(By.ID, 'lblEnganche').text
            # Comisión Apertura
            captionComision = self.driver.find_element(By.ID, 'captionComision').text
            tdComision = self.driver.find_element(By.ID, 'tdComision').text
            # Desembolso Inicial
            captionDesembolso = self.driver.find_element(By.ID, 'captionDesembolso').text
            tdDesembolso = self.driver.find_element(By.ID, 'tdDesembolso').text
            # Monto a Financiar
            tdFinanciar = self.driver.find_element(By.ID, 'tdFinanciar').text
            # Primer Pago
            tdMensualidad = self.driver.find_element(By.ID, 'tdMensualidad').text
            # CAT
            cat = self.driver.find_element(By.XPATH, Locators.cat).text
            print("Sección DETALLE DE FINANCIAMIENTO exitoso")
            quote.scroll_page()
            fname = fake.first_name()
            sname = fake.first_name()
            flastname = fake.last_name()
            slastname = fake.last_name()
            namecomplete = ' '.join([fname, sname, flastname, slastname])
            quote.enter_fname(fname)
            quote.enter_sname(sname)
            quote.enter_flastname(flastname)
            quote.enter_slastname(slastname)
            quote.enter_cellphone("331-698-6302")
            quote.click_cellcompany("NO INFORMADO")
            quote.enter_email("julio.garcia@tekprovider.net")
            time.sleep(1)
            quote.click_aviso_1()
            time.sleep(1)
            quote.click_aviso_2()
            time.sleep(1)
            quote.click_aviso_msj()
            time.sleep(1)
            quote.click_imprimir()
            print("Sección DATOS DEL SOLICITANTE exitoso")

            logging.info("\n******************************** ESCENARIO: %s ********************************\n"
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
                         "- [Comisión Apertura]: %s\n"
                         "- [Desembolso Inicial]: %s\n"
                         "- [Monto a Financiar]: %s\n"
                         "- [Primer Pago]: %s\n"
                         "- [CAT]: %s\n"
                         "- [Nombre Cliente]: %s\n"
                         "- [Cuotas All]: %s\n",
                         fila["var_escenario"], productall, lblcar, lblpricelist, tdaccessoriesamount,
                         tdadditionalcoverageamount, tdextendedwarrantyamount, tdautopartstheftinsuranceamount,
                         tdInsuranceGAPAmount, tdTasa, tdPLazo, lblSeguroVd, tdSeguro,
                         divInsuranceRecipes, lblEnganche, tdComision, tdDesembolso,
                         tdFinanciar,
                         tdMensualidad, cat, namecomplete, cuotasall)
            time.sleep(10)

        except TimeoutException as e:
            error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
            logging.error(error_message)
            print(error_message)
            traceback.print_exc()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
        cls.driver.quit()
        print("Test complete")


if __name__ == '__main__':
    unittest.main()
