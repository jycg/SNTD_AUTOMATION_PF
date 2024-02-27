import time
import sys
import os
import logging
import traceback
from datetime import datetime
from selenium.common import TimeoutException
from faker import Faker

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
fake = Faker()
log_dir = 'C:/Automation_Performance_Sast/app_log'
os.makedirs(log_dir, exist_ok=True)
log_subdir = datetime.now().strftime('%Y-%m-%d')
log_dir = os.path.join(log_dir, log_subdir)
os.makedirs(log_dir, exist_ok=True)
log_filename = os.path.join(log_dir, 'log.txt')
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def cotizador_log(self, drive, fila):
    try:
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
