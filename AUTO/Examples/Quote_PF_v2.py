from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest
from AUTO.PageApp.loginPage import LoginPage
from AUTO.PageApp.searchPage import SearchPage
from AUTO.PageApp.quotePage import QuotePage
from AUTO.Data.database import Database
import xlrd
# import HtmlTestRunner
import sys
import os
from datetime import datetime

# from selenium.common.exceptions import NoSuchElementException

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

data_input = int(input("|Ingresa la cantidad de iteraciones|:\n"))


# data_sheet = int(input("|Cotización|:\n"))

class MyTestCase(unittest.TestCase):
    driver = None
    location_quote = ("C:/Automation_Performance_Sast/SNTD_QUOTE.xls")
    var_excel_quote = xlrd.open_workbook(location_quote)
    template_quote = var_excel_quote.sheet_by_index(0)

    @classmethod
    def setUpClass(cls):
        try:
            # s = Service("C:/Users/jgarcia/PycharmProjects/SNTDProject/drivers/Chrome/114/chromedriver.exe")
            s = "C:/Users/jgarcia/PycharmProjects/SNTDProject/drivers/Edge/116/msedgedriver.exe"
            # cls.driver = webdriver.Chrome(service=s)
            cls.driver = webdriver.Edge(executable_path=s)
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
        except RuntimeError:
            print("Oops!  That was no valid number.  Try again...")

    def test_login_valid(self):

        try:
            database = Database()

            def floatHourToTime(fh):
                hours, hourSeconds = divmod(fh, 1)
                minutes, seconds = divmod(hourSeconds * 60, 1)
                return (int(hours),
                        int(minutes),
                        int(seconds * 60)),

            for cont_input in range(1, data_input):
                print("                                                                    ")
                print("                                                                    ")
                print("********************************** ITERACIÓN # ", cont_input,
                      "**********************************")
                driver = self.driver
                for for_ambiente in range(0, 1):
                    var_ambiente = self.template_quote.cell_value(cont_input, for_ambiente)
                    print("AMBIENTE:", var_ambiente)
                for for_canal in range(1, 2):
                    var_canal = self.template_quote.cell_value(cont_input, for_canal)
                    print("CANAL:", var_canal)
                for for_branch in range(2, 3):
                    var_agencia = self.template_quote.cell_value(cont_input, for_branch)
                    print("----------------- SECCIÓN PRODUCTO -----------------")
                    print("AGENCIA:", var_agencia)
                for for_productofinanciero in range(3, 4):
                    var_productofinanciero = self.template_quote.cell_value(cont_input, for_productofinanciero)
                    print("PRODUCTO FINANCIERO:", var_productofinanciero)
                for for_tipoporducto in range(4, 5):
                    var_tipoproducto = self.template_quote.cell_value(cont_input, for_tipoporducto)
                    print("TIPO DE PRODUCTO:", var_tipoproducto)
                for for_tipouso in range(5, 6):
                    var_tipouso = self.template_quote.cell_value(cont_input, for_tipouso)
                    print("TIPO USO:", var_tipouso)
                for for_tipopersona in range(6, 7):
                    var_tipopersona = self.template_quote.cell_value(cont_input, for_tipopersona)
                    print("TIPO PERSONA:", var_tipopersona)
                for for_tipocredito in range(7, 8):
                    var_tipocredito = self.template_quote.cell_value(cont_input, for_tipocredito)
                    print("TIPO CRÉDITO:", var_tipocredito)
                print("---------- SECCIÓN PLAN DE FINANCIAMIENTO ----------")
                for for_plan in range(8, 9):
                    var_plan = self.template_quote.cell_value(cont_input, for_plan)
                    print("PLAN:", var_plan)
                for for_acce in range(9, 10):
                    var_accesorios = self.template_quote.cell_value(cont_input, for_acce)
                    print("ACCESORIOS", var_accesorios)
                for for_monto_acce in range(10, 11):
                    var_montoaccesorios = self.template_quote.cell_value(cont_input, for_monto_acce)
                    print("MONTO ACCESORIOS:", var_montoaccesorios)
                for for_type_acce in range(11, 12):
                    var_formadepago = self.template_quote.cell_value(cont_input, for_type_acce)
                    print("FORMA DE PAGO:", var_formadepago)
                for for_plazo in range(12, 13):
                    var_plazo = int(self.template_quote.cell_value(cont_input, for_plazo))
                    cuota_ = "{}{}".format("divTermContent_", int(var_plazo))
                    str_monto = str(cuota_)
                    print("PLAZO:", var_plazo)
                    time.sleep(1)
                    driver.quit()
                for for_ge in range(13, 14):
                    var_ge = self.template_quote.cell_value(cont_input, for_ge)
                    print("GARANTÍA EXTENDIDAE:", var_ge)
                for for_sra in range(14, 15):
                    var_sra = self.template_quote.cell_value(cont_input, for_sra)
                    print("SEGURO ROBO DE AUTOPARTES:", var_sra)
                for for_gap in range(15, 16):
                    var_gap = self.template_quote.cell_value(cont_input, for_gap)
                    print("GARANTÍA EXTENDIDAE:", var_gap)
                    print("------------------ SEGURO DE AUTO ------------------")
                for for_insurance in range(16, 17):
                    var_seguro = self.template_quote.cell_value(cont_input, for_insurance)
                    print("SEGURO DE DAÑOS:", var_seguro)
                for for_formapago in range(17, 18):
                    var_formadepagoseguro = self.template_quote.cell_value(cont_input, for_formapago)
                    print("FORMA DE PAGO:", var_formadepagoseguro)
                for for_tiposeguro in range(18, 19):
                    var_tiposeguro = self.template_quote.cell_value(cont_input, for_tiposeguro)
                    print("TIPO:", var_tiposeguro)
                for for_cp in range(19, 20):
                    var_cp = int(self.template_quote.cell_value(cont_input, for_cp))
                    cp_ = "{}{}".format("", int(var_cp))
                    str_cp = str(cp_)
                    print("CÓDIGO POSTAL:", str_cp)
                for for_cobertura in range(20, 21):
                    var_cobertura = self.template_quote.cell_value(cont_input, for_cobertura)
                    print("COBERTURA:", var_cobertura)
                for for_fechanac in range(21, 22):
                    var_fechanac = self.template_quote.cell_value(cont_input, for_fechanac)
                    # datet = datetime.strftime(var_fechanac, "%d-%b-%Y")
                    # print("FECHA DE NACIMIENTO:", datet.strptime("%d-%b-%Y"))

                    # dt = datetime.fromordinal(datetime(1900,1,1).toordinal() + int(var_fechanac) - 2)
                    # hour, minute, second = floatHourToTime(var_fechanac % 1)
                    # dt = dt.replace(hour=hour, minute=minute, second=second)
                    date_fechanac = datetime(*xlrd.xldate_as_tuple(var_fechanac, 0))
                    fechanac = date_fechanac.strftime("%d/%m/%Y")
                    print("FECHA DE NACIMIENTO:", fechanac)
                for for_sexo in range(22, 23):
                    var_sexo = self.template_quote.cell_value(cont_input, for_sexo)
                    print("SEXO:", var_sexo)

                    #Termina for para leer información del excel
                    print("***********************************************************************************")

                    if self.template_quote.cell_value(cont_input, data_input) == "TEST1":
                        driver.get("https://sntdtest.tekprovider.net:9444/TekFinauto/Autogestion/Acceso/Login")
                    elif self.template_quote.cell_value(cont_input, for_ambiente) == "TEST2":
                        driver.get("https://sntdqa.tekprovider.net:9081/TekFinauto/Autogestion/Acceso/Login")
                    elif self.template_quote.cell_value(cont_input, for_ambiente) == "UAT1":
                        driver.get("http://192.168.30.225:83/TekFinauto/Autogestion/Acceso/Login")
                    elif self.template_quote.cell_value(cont_input, for_ambiente) == "UAT2":
                        driver.get("http://192.168.30.225:92/TekFinauto/Autogestion/Acceso/Login")
                    elif self.template_quote.cell_value(cont_input, for_ambiente) == "PRE":
                        driver.get("https://gcscreditoautobo.pre.mx.corp/TekFinauto/autogestion/Acceso/Login")
                    elif self.template_quote.cell_value(cont_input, for_ambiente) == "PROD":
                        driver.get("https://www.autocredit-santander.com.mx/TekFinauto/AUTOGESTION/authentication")
                    elif self.template_quote.cell_value(cont_input, for_ambiente) == "DEV":
                        driver.get("http://192.168.30.80:92/tekfinauto/autogestion/acceso/login")
                    else:
                        print(
                            "No seleccionaste un ambiente. Verifica tu configuración y selecciona el ambiente deseado")
                        driver.close()
                        driver.quit()
                    print("AMBIENTE:", self.template_quote.cell_value(cont_input, for_ambiente))
                    # driver.execute_script('window.scrollBy(0, 500);')
                    time.sleep(3)
                    driver.quit()

                    # quote.click_accesorios_type('{:d}'.format(self.template_quote.cell_value(cont_input,for_plazo)))
                    #  print(self.template_quote.cell_value(cont_input, for_plazo))
                    #  monto_vehiculo = self.driver.find_element(By.ID,'input-as-label-operator').get_attribute("value")
                    #  c_monto_vehiculo = "${:,.2f}".format(float(monto_vehiculo))
                    #  print("MONTO VEHÍCULO", c_monto_vehiculo)
                    #
                    #  enganche = 10.0
                    #  monto_enganche = int(float(monto_vehiculo)) * 0.10
                    #  print("ENGANCHE: ", "${:,.2f}".format(monto_enganche))
                    #  print("PROCENTAJE ENGANCHE: ",enganche % int(float(monto_vehiculo)),"%")
                    #  quote.click_cuotas_select()
                    #
                    #  time.sleep(2)
                    #  quote.click_insurance_no()
                    #  time.sleep(2)
                    #  quote.click_msj_no()

                    #
                    # # QUOTE - PRODUCTO
                    # time.sleep(2)
                    #
                    # print("_________________Ejemplo:", self.template_quote.cell_value(cont_input, for_tipoporducto))
        except ValueError:
            print("Ocurrió un error, intenta de nuevo por favor.")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
        cls.driver.quit()
        print("Test complete")


if __name__ == '__main__':
    unittest.main()
