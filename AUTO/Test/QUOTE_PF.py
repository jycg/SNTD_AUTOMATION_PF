import re
import time
import unittest
import sys
import os
import xlrd
import logging
import traceback
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
from AUTO.Test.SOL_DATOS_PERSONALES import MyTestCaseSolicitud

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

    @classmethod
    def setUpClass(cls):
        s = "C:/Users/jgarcia/PycharmProjects/SNTDProject/drivers/Edge/119/msedgedriver.exe"
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

    def test_login_valid(self):
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
                "var_tbl_amortiza": sheet_quote.cell_value(numero_fila, 35),
                "var_crearsolicitud": sheet_quote.cell_value(numero_fila, 36),
            }
            print(fila)
            try:
                self.realizar_acciones_con_fila(fila, fila_environment)
            except Exception as e:
                error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
                logging.error(error_message)
                print(error_message)
                # traceback.print_exc()

    def realizar_acciones_con_fila(self, fila, fila_environment):
        # MyTestCaseSolicitud.datos_personales(unittest.TestCase)
        commentgap = ""
        commentge = ""
        commentrsa = ""
        try:
            print("                                                                    ")
            print("\033[1;32m*" * 30 + " ESCENARIO # ", fila["var_escenario"], "*\033[0m" * 30)
            driver = self.driver
            if fila_environment["var_environment"] == "BYD_QA":
                if fila["var_producto_finan"] == "ARRENDAMIENTO" or fila["var_tipo_uso"] == "CHOFER PRVADO" or fila["var_tipo_uso"] == "COMERCIAL" or \
                        fila["var_tipo_producto"] == "SEMINUEVO" or fila["var_tipo_producto"] == "MOTO" or fila["var_marca"] != "BYD":
                    print("La configuración no forma parte del proyecto, revisa los datos e intenta de nuevo")
                    driver.close()
                    driver.quit()
            else:
                pass
            driver.get(fila_environment["var_url"])
            login = LoginPage(driver)
            search = SearchPage(driver)
            quote = QuotePage(driver)

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

            # Producto Financiero
            if fila["var_producto_finan"] == "ARRENDAMIENTO":
                quote.click_arrendamiento()
            else:
                pass

            # Tipo de Producto
            if fila["var_tipo_producto"] == "NUEVO":
                if fila_environment["var_environment"] == "BYD_QA":
                    quote.click_tipon_BYD()
                elif fila_environment["var_environment"] == "OM2":
                    quote.click_tipon_OM()
                else:
                    quote.click_tipon()
            elif fila["var_tipo_producto"] == "SEMINUEVO":
                if fila_environment["var_environment"] == "BYD_QA":
                    pass
                elif fila_environment["var_environment"] == "OM2":
                    quote.click_tipos_OM()
                else:
                    quote.click_tipos()
            else:
                if fila_environment["var_environment"] == "BYD_QA":
                    pass
                elif fila_environment["var_environment"] == "OM2":
                    quote.click_tipom_OM()
                else:
                    quote.click_tipom()

            # Uso
            if fila["var_tipo_uso"] == "PARTICULAR":
                if fila_environment["var_environment"] == "BYD_QA":
                    quote.click_uso_p_BYD()
                elif fila_environment["var_environment"] == "OM2":
                    pass
                else:
                    quote.click_uso_p()
            elif fila["var_tipo_uso"] == "CHOFER PRVADO":
                if fila_environment["var_environment"] == "BYD_QA":
                    pass
                elif fila_environment["var_environment"] == "OM2":
                    pass
                else:
                    quote.click_uso_cp()
            else:
                if fila_environment["var_environment"] == "BYD_QA":
                    pass
                elif fila_environment["var_environment"] == "OM2":
                    pass
                else:
                    quote.click_uso_c()

            # Tipo de persona
            if fila["var_tipo_persona"] == "FISICA":
                if fila_environment["var_environment"] == "BYD_QA":
                    quote.click_p_f_BYD()
                elif fila_environment["var_environment"] == "OM2":
                    quote.click_p_f_OM()
                else:
                    quote.click_p_f()
            else:
                if fila_environment["var_environment"] == "BYD_QA":
                    quote.click_p_fae_BYD()
                elif fila_environment["var_environment"] == "OM2":
                    quote.click_p_fae_OM()
                else:
                    quote.click_p_fae()

            time.sleep(1)
            quote.click_marca()

            quote.enter_marca(fila["var_marca"])
            time.sleep(1)
            quote.click_modelo()
            quote.enter_modelo(fila["var_modelo"])
            time.sleep(1)
            quote.click_version()
            quote.enter_version(fila["var_version"])
            time.sleep(1)
            quote.click_ano()
            quote.enter_anio(fila["var_ano"])
            if fila["var_tipo_producto"] == "SEMINUEVO":
                quote.click_monto_vehiculo()
                time.sleep(1)
                quote.control_monto_vehiculo()
                time.sleep(1)
                quote.clear_monto_vehiculo()
                time.sleep(2)
                quote.enter_monto_vehiculo("$810,900.00")
            else:
                pass

            print("\033[1;32m-" * 1 + " PRODUCTO EXITOSO " + "-\033[0m" * 1)
            quote.click_section_divListPrice()
            time.sleep(3)

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
                        commentge = "Estás tratando de seleccionar garantía extendida pero no está configurado en el plan financiero"
                else:
                    pass

                if fila["var_seguro_robo_aut"] == "SI":
                    try:
                        quote.click_SRA()
                    except NoSuchElementException:
                        commentrsa = "Estás tratando de seleccionar seguro de robo autopartes pero no está configurado en el plan financiero"
                else:
                    quote.click_label()

                if fila["var_gap"] == "SI":

                    try:
                        quote.click_GaP()
                    except NoSuchElementException:
                        commentgap = "Estás tratando de seleccionar seguro GaP pero no está configurado en el plan financiero"

                else:
                    quote.click_label()

                time.sleep(2)
                quote.click_aceptar_msj_gap()
                driver.execute_script('window.scrollBy(0, 500);')
                print("\033[1;32m-" * 1 + " COBERTURAS ADICIONALES EXITOSO " + "-\033[0m" * 1)

            # Obtiene la fecha del excel y lo convierte a formato "fecha"
            fecha_excel = datetime.fromordinal(
                datetime(1900, 1, 1).toordinal() + int(fila["var_fecha"]) - 2)

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

            time.sleep(1)

            # Producto
            productall = "Prodcuto financiero: {}, Tipo de Producto: {}, Uso: {}, Tipo de Persona: {}" \
                .format(fila["var_producto_finan"], fila["var_tipo_producto"], fila["var_tipo_uso"], fila["var_tipo_persona"])
            # Cuota
            # try:
            #     txtpay12: str = self.driver.find_element(By.XPATH, Locators.txtPay12).text
            # except NoSuchElementException:
            #     txtpay12 = "El plaso no está configurado en el plan"
            # try:
            #     txtpay24: str = self.driver.find_element(By.XPATH, Locators.txtPay24).text
            # except NoSuchElementException:
            #     txtpay24 = "El plaso no está configurado en el plan"
            # try:
            #     txtpay36: str = self.driver.find_element(By.XPATH, Locators.txtPay36).text
            # except NoSuchElementException:
            #     txtpay36 = "El plaso no está configurado en el plan"
            # try:
            #     txtpay48: str = self.driver.find_element(By.XPATH, Locators.txtPay48).text
            # except NoSuchElementException:
            #     txtpay48 = "El plaso no está configurado en el plan"
            # try:
            #     txtpay60: str = self.driver.find_element(By.XPATH, Locators.txtPay60).text
            # except NoSuchElementException:
            #     txtpay60 = "El plaso no está configurado en el plan"
            # try:
            #     txtpay72: str = self.driver.find_element(By.XPATH, Locators.txtPay72).text
            # except NoSuchElementException:
            #     txtpay72 = "El plaso no está configurado en el plan"
            #
            # cuotasall = "Cuota 12: {}, Cuota 24: {}, Cuota 36: {}, Cuota 48: {}, Cuota 60: {}, Cuota 72: {}" \
            #     .format(txtpay12, txtpay24, txtpay36, txtpay48, txtpay60, txtpay72)

            cuotasdetail = {}
            cuotas_detail = {
                "Cuota 12": Locators.txtPay12,
                "Cuota 24": Locators.txtPay24,
                "Cuota 36": Locators.txtPay36,
                "Cuota 48": Locators.txtPay48,
                "Cuota 60": Locators.txtPay60,
                "Cuota 72": Locators.txtPay72
            }
            for cuotas__, cuota__ in cuotas_detail.items():
                try:
                    cuotasdetail[cuotas__] = self.driver.find_element(By.XPATH, cuota__).text
                except NoSuchElementException:
                    cuotasdetail[cuotas__] = f"El plaso no está configurado en el plan"
            cuotasall = "Cuota 12: {Cuota 12}, Cuota 24: {Cuota 24}, Cuota 36: {Cuota 36}, Cuota 48: {Cuota 48}, Cuota 60: {Cuota 60}, Cuota 72: {Cuota 72}".format(**cuotasdetail)
            # Vehículo
            lblcar: str = self.driver.find_element(By.ID, Locators.amortizationdetail_lblCar).text
            # Valor del Vehículo
            lblpricelist: str = self.driver.find_element(By.ID, Locators.amortizationdetail_lblPriceList).text
            # Accesorios Vehículo
            tdaccessoriesamount: str = self.driver.find_element(By.ID, 'tdAccessoriesAmount').text
            # Coberturas Adicionales
            tdadditionalcoverageamount: str = self.driver.find_element(By.ID, 'tdAdditionalCoverageAmount').text
            # Garantía Extendida
            tdextendedwarrantyamount: str = self.driver.find_element(By.ID, 'tdExtendedWarrantyAmount').text
            # Seguro de Robo de Autopartes
            tdautopartstheftinsuranceamount: str = self.driver.find_element(By.ID, 'tdAutoPartsTheftInsuranceAmount').text
            # Seguro GAP
            tdInsuranceGAPAmount: str = self.driver.find_element(By.ID, 'tdInsuranceGAPAmount').text
            # Tasa Fija
            tdTasa: str = self.driver.find_element(By.ID, 'tdTasa').text  # Plazo
            tdPLazo = self.driver.find_element(By.ID, 'tdPLazo').text
            # Seguro de Vida y Desempleo
            lblSeguroVd = self.driver.find_element(By.ID, 'lblSeguroVd').text
            # Seguro del vehículo Año 1
            tdSeguro = self.driver.find_element(By.ID, 'tdSeguro').text

            def limpiar_subsecuente(texto):
                texto_limpio = re.sub(r'[^\d.]+', '', texto)
                return texto_limpio

            try:
                # Intenta encontrar el elemento divInsuranceRecipes
                divInsuranceRecipes = self.driver.find_element(By.ID, 'divInsuranceRecipes').text
                divInsuranceRecipes_v2 = limpiar_subsecuente(divInsuranceRecipes)
                replace_divInsuranceRecipes: str = divInsuranceRecipes_v2
            except NoSuchElementException:
                replace_divInsuranceRecipes = "No hay información disponible en divInsuranceRecipes"

            # Enganche
            lblEnganche = self.driver.find_element(By.ID, 'lblEnganche').text
            # Monto VFG y Balloon
            try:
                ballon_and_tcm = self.driver.find_element(By.ID, Locators.amortizationdetail_balloonTCMInfo).text
            except NoSuchElementException:
                ballon_and_tcm = "Balloon - TCM: No contiene información"

            # Tasa Fija Ciclo 2
            try:
                tasaC2 = driver.find_element(By.ID, Locators.amortizationdetail_tdInterestRateTCM).text
            except NoSuchElementException:
                tasaC2 = ''

            # Plazo Ciclo 2
            try:
                plazoC2 = driver.find_element(By.ID, Locators.amortizationdetail_tdTermTCM).text
            except NoSuchElementException:
                plazoC2 = ''

            # Comisión Apertura
            tdComision = self.driver.find_element(By.ID, 'tdComision').text
            # Desembolso Inicial
            tdDesembolso = self.driver.find_element(By.ID, 'tdDesembolso').text
            # Monto a Financiar
            tdFinanciar = self.driver.find_element(By.ID, 'tdFinanciar').text
            # Primer Pago
            tdMensualidad = self.driver.find_element(By.ID, 'tdMensualidad').text
            # CAT
            cat = self.driver.find_element(By.XPATH, Locators.cat).text
            print("\033[1;32m-" * 1 + " DETALLE DE FINANCIAMIENTO Y TABLA DE AMORTIZACIÓN EXITOSO " + "-\033[0m" * 1)

            TblamortizationTCM = "No es visible"
            Tblamortization = "No es visible"
            if fila["var_tbl_amortiza"] == "SI":

                Tblamortization = driver.find_element(By.ID, Locators.tblAmortization_information).text
                try:
                    TblamortizationTCM = driver.find_element(By.ID, Locators.tblAmortizationCycle2_TCM).text
                except NoSuchElementException:
                    TblamortizationTCM = 'Tabla de Amortización C2: No contiene información'
            else:
                pass

            quote.scroll_page()

            # Sección DATOS DEL SOLICITANTE
            if fila["var_faker"] == "SI":
                fname = fake.first_name()
                sname = fake.first_name()
                flastname = fake.last_name()
                slastname = fake.last_name()
            else:
                fname = "JULIO"
                sname = "DE JESUS"
                flastname = "GARCIA"
                slastname = "HERNANDEZ"

            quote.enter_fname(fname)
            quote.enter_sname(sname)
            quote.enter_flastname(flastname)
            quote.enter_slastname(slastname)
            namecomplete = ' '.join([fname, sname, flastname, slastname])
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
            time.sleep(1)
            element_msj = driver.find_element(By.XPATH, Locators.alert_label)
            if element_msj.is_displayed():
                quote.click_aceptar_msj_gap()
            else:
                pass

            print("\033[1;32m-" * 1 + " DATOS DEL SOLICITANTE EXITOSO " + "-\033[0m" * 1)
            comments_all = "GAP: {}, SRA: {}, GE: {}".format(commentgap, commentrsa, commentge)
            # Guarda información en el log
            logging.info("*" * 45 + " ESCENARIO: %s " + "*" * 45 + "\n"
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
                                                                   f"- [{ballon_and_tcm}] %s\n"
                                                                   "- [Tasa Fija Ciclo 2]: %s\n"
                                                                   "- [Plazo Ciclo 2]: %s\n"
                                                                   "- [Comisión Apertura]: %s\n"
                                                                   "- [Desembolso Inicial]: %s\n"
                                                                   "- [Monto a Financiar]: %s\n"
                                                                   "- [Primer Pago]: %s\n"
                                                                   "- [CAT]: %s\n"
                                                                   "- [Nombre Cliente]: %s\n"
                                                                   "- [Cuotas All]: %s\n"
                                                                   "- [Tabla de Amortización]: %s\n"
                                                                   f"- [{TblamortizationTCM}] %s\n"
                                                                   "- [Comentarios generales]: %s\n",
                         fila["var_escenario"], productall, lblcar, lblpricelist, tdaccessoriesamount, tdadditionalcoverageamount, tdextendedwarrantyamount, tdautopartstheftinsuranceamount,
                         tdInsuranceGAPAmount, tdTasa, tdPLazo, lblSeguroVd, tdSeguro, replace_divInsuranceRecipes, lblEnganche, '', tasaC2, plazoC2, tdComision, tdDesembolso, tdFinanciar,
                         tdMensualidad, cat, namecomplete, cuotasall, Tblamortization, '', comments_all)
            print("\033[1;32m-" * 1 + " FINISHED COTIZACIÓN" + "-\033[0m" * 1)
            time.sleep(10)

            if fila["var_crearsolicitud"] == "NO":
                pass
            else:
                print("\033[1;32m-" * 30 + " START SOLICITUD" + "-\033[0m" * 30)
                quote.click_solicita_credito()
                time.sleep(1)
                quote.click_si_confirm()

                element_code = driver.find_element(By.XPATH, Locators.quote_divCodigoVerTemp)
                element_code_text = driver.execute_script('return arguments[0].innerText;', element_code)
                print(element_code_text)

                time.sleep(1)
                quote.codigo_verificacion(element_code_text)
                time.sleep(1)
                quote.click_btnGotoCreditform()
                time.sleep(5)

                callsolicitud = MyTestCaseSolicitud()
                callsolicitud.datos_personales()

        except TimeoutException as e:
            error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
            logging.error(error_message)
            # print(error_message)

    traceback.print_exc()

    def tearDown(self):
        try:
            time.sleep(1)
            self.driver.close()
            self.driver.quit()
            time.sleep(2)
        except Exception as e:
            error_message = f"Error en el escenario : {str(e)}"
            logging.error(error_message)
            # print(f"Error al cerrar el navegador: {e}")


if __name__ == '__main__':
    unittest.main()
