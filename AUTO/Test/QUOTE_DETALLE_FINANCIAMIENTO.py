import re
import time
import sys
import os
import logging
import traceback
from datetime import datetime
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
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


def cotizador_detalle_financiamiento(self, driver, fila):
    try:
        # Producto
        self.productall = "Prodcuto financiero: {}, Tipo de Producto: {}, Uso: {}, Tipo de Persona: {}" \
            .format(fila["var_producto_finan"], fila["var_tipo_producto"], fila["var_tipo_uso"], fila["var_tipo_persona"])
        # Cuota
        try:
            txtpay12: str = self.driver.find_element(By.XPATH, Locators.txtPay12).text
        except NoSuchElementException:
            txtpay12 = "El plaso no está configurado en el plan"
        try:
            txtpay24: str = self.driver.find_element(By.XPATH, Locators.txtPay24).text
        except NoSuchElementException:
            txtpay24 = "El plaso no está configurado en el plan"
        try:
            txtpay36: str = self.driver.find_element(By.XPATH, Locators.txtPay36).text
        except NoSuchElementException:
            txtpay36 = "El plaso no está configurado en el plan"
        try:
            txtpay48: str = self.driver.find_element(By.XPATH, Locators.txtPay48).text
        except NoSuchElementException:
            txtpay48 = "El plaso no está configurado en el plan"
        try:
            txtpay60: str = self.driver.find_element(By.XPATH, Locators.txtPay60).text
        except NoSuchElementException:
            txtpay60 = "El plaso no está configurado en el plan"
        try:
            txtpay72: str = self.driver.find_element(By.XPATH, Locators.txtPay72).text
        except NoSuchElementException:
            txtpay72 = "El plaso no está configurado en el plan"

        self.cuotasall = "Cuota 12: {}, Cuota 24: {}, Cuota 36: {}, Cuota 48: {}, Cuota 60: {}, Cuota 72: {}" \
            .format(txtpay12, txtpay24, txtpay36, txtpay48, txtpay60, txtpay72)
        time.sleep(1)

        # Vehículo
        self.lblcar = self.driver.find_element(By.ID, Locators.amortizationdetail_lblCar).text
        # Valor del Vehículo
        self.lblpricelist = self.driver.find_element(By.ID, Locators.amortizationdetail_lblPriceList).text
        # Accesorios Vehículo
        self.tdaccessoriesamount = self.driver.find_element(By.ID, 'tdAccessoriesAmount').text
        # Coberturas Adicionales
        self.tdadditionalcoverageamount = self.driver.find_element(By.ID, 'tdAdditionalCoverageAmount').text
        # Garantía Extendida
        self.tdextendedwarrantyamount = self.driver.find_element(By.ID, 'tdExtendedWarrantyAmount').text
        # Seguro de Robo de Autopartes
        self.tdautopartstheftinsuranceamount = self.driver.find_element(By.ID, 'tdAutoPartsTheftInsuranceAmount').text
        # Seguro GAP
        self.tdInsuranceGAPAmount = self.driver.find_element(By.ID, 'tdInsuranceGAPAmount').text
        # Tasa Fija
        self.tdTasa = self.driver.find_element(By.ID, 'tdTasa').text
        # Plazo
        self.tdPLazo = self.driver.find_element(By.ID, 'tdPLazo').text
        # Seguro de Vida y Desempleo
        self.lblSeguroVd = self.driver.find_element(By.ID, 'lblSeguroVd').text
        # Seguro del vehículo Año 1
        self.tdSeguro = self.driver.find_element(By.ID, 'tdSeguro').text

        def limpiar_subsecuente(texto):
            texto_limpio = re.sub(r'[^\d.]+', '', texto)
            return texto_limpio

        try:
            # Intenta encontrar el elemento divInsuranceRecipes
            divInsuranceRecipes = self.driver.find_element(By.ID, 'divInsuranceRecipes').text
            divInsuranceRecipes_v2 = limpiar_subsecuente(divInsuranceRecipes)
            self.replace_divInsuranceRecipes = divInsuranceRecipes_v2
        except NoSuchElementException:
            self.replace_divInsuranceRecipes = "No hay información disponible en divInsuranceRecipes"

        # Enganche
        self.lblEnganche = self.driver.find_element(By.ID, 'lblEnganche').text
        # Monto VFG y Balloon
        try:
            self.ballon_and_tcm = self.driver.find_element(By.ID, Locators.amortizationdetail_balloonTCMInfo).text
        except NoSuchElementException:
            self.ballon_and_tcm = "Balloon - TCM: No contiene información"

        # Tasa Fija Ciclo 2
        try:
            self.tasaC2 = driver.find_element(By.ID, Locators.amortizationdetail_tdInterestRateTCM).text
        except NoSuchElementException:
            self.tasaC2 = ''

        # Plazo Ciclo 2
        try:
            self.plazoC2 = driver.find_element(By.ID, Locators.amortizationdetail_tdTermTCM).text
        except NoSuchElementException:
            self.plazoC2 = ''

        # Comisión Apertura
        self.tdComision = self.driver.find_element(By.ID, 'tdComision').text
        # Desembolso Inicial
        self.tdDesembolso = self.driver.find_element(By.ID, 'tdDesembolso').text
        # Monto a Financiar
        self.tdFinanciar = self.driver.find_element(By.ID, 'tdFinanciar').text
        # Primer Pago
        self.tdMensualidad = self.driver.find_element(By.ID, 'tdMensualidad').text
        # CAT
        self.cat = self.driver.find_element(By.XPATH, Locators.cat).text
        print("\033[1;32m-" * 1 + " DETALLE DE FINANCIAMIENTO Y TABLA DE AMORTIZACIÓN EXITOSO " + "-\033[0m" * 1)

        self.TblamortizationTCM = "No es visible"
        self.Tblamortization = "No es visible"
        if fila["var_tbl_amortiza"] == "SI":
            self.Tblamortization = driver.find_element(By.ID, Locators.tblAmortization_information).text
            try:
                self.TblamortizationTCM = driver.find_element(By.ID, Locators.tblAmortizationCycle2_TCM).text
            except NoSuchElementException:
                self.TblamortizationTCM = 'Tabla de Amortización C2: No contiene información'
        else:
            pass
    except TimeoutException as e:
        error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
        logging.error(error_message)
        traceback.print_exc()
