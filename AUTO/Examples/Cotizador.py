from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import unittest
from AUTO.PageApp.loginPage import LoginPage
from AUTO.PageApp.searchPage import SearchPage
from AUTO.PageApp.quotePage import QuotePage
from AUTO.Data.database import Database
import xlrd
import HtmlTestRunner
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

# NOTA: Las celdas de color azul no debe eliminarse debido a que es la base. Para los ciclos en PyCharm, se sugiere
# iniciarlizar la variable con el valor 2 para iniciar con el registro de operaciones


print("|-------------------------------------------------------------------------------------------|")
print("|A continuación seleccionarás algunos datos para registrar tus cotizaciones:                |")
print("|Nota: solo debes de ingresar números para seleccionar la información que se necesita.      |")
print("|Adicional, asegúrate que la cantidad de iteraciones sea la misma que se tenga en el excel. |")
print("|-------------------------------------------------------------------------------------------|")
# imput_environment = int(input("|AMBIENTE: [1 - TEST, 2 - UAT1, 3 - UAT2, 4 - PRE, 5 - DEV"))
data_input = int(
    input("|Ingresa la cantidad de iteraciones                                                         |:\n"))
input_environment = int(
    input("|AMBIENTE: [1 - TEST, 2 - UAT1, 3 - UAT2, 4 - PRE, 5 - DEV]                                |:\n"))
# input_user = int(input("|USUARIO: [1 - TBBT01, 2 - TBBT02, 3 - n807433, 4 - n807322]                                |:\n"))
# input_product = int(input("|PRODUCTO: [1 - CREDITO, 2 - ARRENDAMIENTO]                                                 |:\n"))
# input_typeproduct = int(
#     input("|TIPO PRODUCTO: [1 - NUEVO, 2 - SEMINUEVO, 3 - MOTO]                                        |:\n"))
# input_typeuse = int(
#     input("|TIPO USO: [1 - PARTICULAR, 2 - CHOFER, 3 - COMERCIAL]                                      |:\n"))
# input_typepeople = int(
#     input("|PRODUCTO: [1 - FISICA, 2 - FISICA AE]                                                      |:\n"))
print("|-------------------------------------------------------------------------------------|")


class CotizadorTest(unittest.TestCase):
    location_quote = ("C:/Automation_Performance_Sast/QUOTE.xls")
    var_excel_quote = xlrd.open_workbook(location_quote)
    template_quote = var_excel_quote.sheet_by_index(0)

    @classmethod
    def setUpClass(cls):
        s = Service("C:/Users/jgarcia/PycharmProjects/SNTDProject/drivers/110/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):

        database = Database()

        # Condición donde se manda el valor para indicar la cantidad de operaciones a registrar. Iniciando desde la fila 3 del excel.
        for cont_input in range(1, data_input):
            print("Cliente:", cont_input)

            driver = self.driver

            # Condición para determinar que ambiente se seleccionó desde consola
            if database.environmentnstd((input_environment)) == "TEST":
                driver.get("https://sntdtest.tekprovider.net:9444/TekFinauto/Autogestion/Acceso/Login")
            elif database.environmentnstd((input_environment)) == "UAT1":
                driver.get("http://192.168.30.225:83/TekFinauto/autogestion/Acceso/Login")
            elif database.environmentnstd((input_environment)) == "UAT2":
                driver.get("http://192.168.30.225:92/TekFinauto/Autogestion/Acceso/Login")
            elif database.environmentnstd((input_environment)) == "PRE":
                driver.get("https://gcscreditoautobo.pre.mx.corp/TekFinauto/autogestion/Acceso/Login")
            elif database.environmentnstd((input_environment)) == "DEV":
                driver.get("http://192.168.30.80:92/tekfinauto/Autogestion/Acceso/Login")
            else:
                print("Intenta de nuevo")

            # Login
            login = LoginPage(driver)
            for for_user in range(0, 1):
                login.enter_username(self.template_quote.cell_value(cont_input, for_user))
                login.enter_password("S1santan")
                login.click_login()

                # Search
                search = SearchPage(driver)
                search.click_nvaCot()

                # Quote - PRODUCTO
                # Condición para obtener el producto financiero
                quote = QuotePage(driver)
                for for_typecredit in range(1, 2):
                    if self.template_quote.cell_value(cont_input, for_typecredit) == "CREDITO":
                        quote.click_credito()
                    else:
                        quote.click_arrendamiento()

                        # Condición para obtener el tipo de producto
                        for for_typeproduct in range(2, 3):
                            if self.template_quote.cell_value(cont_input, for_typeproduct) == "NUEVO":
                                quote.click_tipon()
                            elif self.template_quote.cell_value(cont_input, for_typeproduct) == "SEMINUEVO":
                                quote.click_tipos()
                            else:
                                quote.click_tipom()

                            time.sleep(5)
                            driver.quit()
                        # Condición para obtener la marca configurada en el excel
                        for for_marca in range(2, 3):
                            time.sleep(2)
                            quote.click_marca()
                            quote.enter_marca(self.template_quote.cell_value(cont_input, for_marca))
                    for for_modelo in range(3, 4):
                        time.sleep(2)
                        quote.click_modelo()
                        quote.enter_modelo(self.template.cell_value(cont_input, for_modelo))
                        for for_version in range(8, 9):
                            time.sleep(2)
                            quote.click_version()
                            quote.enter_version(self.template.cell_value(cont_input, for_version))
                            for for_ano in range(9, 10):
                                time.sleep(2)
                                quote.click_ano()
                                quote.enter_ano(self.template.cell_value(cont_input, for_ano))
                                time.sleep(20)
                                quote.get_monto_vehiculo()
                                print(quote.get_monto_vehiculo())
                                # Quote - PLAN
                                for for_plan in range(10, 11):
                                    time.sleep(2)
                                    quote.click_plan(self.template.cell_value(cont_input, for_plan))
                                    for for_enganche in range(11, 12):
                                        time.sleep(2)
                                        quote.enter_enganche(self.template.cell_value(cont_input, for_enganche))
                                        time.sleep(5)
                                        quote.click_cuotas_show()
                                        for for_plazo in range(18, 19):
                                            time.sleep(3)
                                            quote.click_cuotas_select()
                                            time.sleep(7)
                                            # Quote - SEGURO
                                            quote.click_insurance_no()
                                            time.sleep(2)
                                            quote.click_msj_no()
                                            # Quote - INFORMACIÓN CLIENTE
                                            time.sleep(10)
                                            quote.scroll_page()
                                            time.sleep(2)
                                            for for_fname in range(26, 27):
                                                quote.enter_fname(self.template.cell_value(cont_input, for_fname))
                                                for for_sname in range(27, 28):
                                                    quote.enter_sname(self.template.cell_value(cont_input, for_sname))
                                                    for for_flastname in range(28, 29):
                                                        quote.enter_flastname(
                                                            self.template.cell_value(cont_input, for_flastname))
                                                        for for_slastname in range(29, 30):
                                                            quote.enter_slastname(
                                                                self.template.cell_value(cont_input, for_slastname))
                                                            for for_lada in range(30, 31):
                                                                quote.enter_lada(
                                                                    self.template.cell_value(cont_input, for_lada))
                                                                for for_phone in range(31, 32):
                                                                    quote.enter_phone(
                                                                        self.template.cell_value(cont_input, for_phone))
                                                                    for for_cellphone in range(32, 33):
                                                                        quote.enter_cellphone(
                                                                            self.template.cell_value(cont_input,
                                                                                                     for_cellphone))
                                                                        for for_company in range(33, 34):
                                                                            quote.click_cellcompany(
                                                                                self.template.cell_value(cont_input,
                                                                                                         for_company))
                                                                            for for_email in range(34, 35):
                                                                                quote.enter_email(
                                                                                    self.template.cell_value(cont_input,
                                                                                                             for_email))
                                                                                time.sleep(5)
                                                                                quote.click_aviso_1()
                                                                                time.sleep(1)
                                                                                quote.click_aviso_2()
                                                                                time.sleep(1)
                                                                                quote.click_aviso_msj()
                                                                                time.sleep(3)
                                                                                quote.click_imprimir()
                                                                                time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        time.time(7)
        cls.driver.close()
        cls.driver.quit()
        print("Test Quote complete")

    if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
            output='C:/Users/jgarcia/PycharmProjects/SNTDProject/AUTO/reports'))
