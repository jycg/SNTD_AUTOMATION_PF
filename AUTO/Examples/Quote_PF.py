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
# from selenium.common.exceptions import NoSuchElementException

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

data_input = int(input("|Ingresa la cantidad de iteraciones|:\n"))


# data_sheet = int(input("|Cotización|:\n"))

class MyTestCase(unittest.TestCase):
    location_quote = ("C:/Automation_Performance_Sast/SNTD_QUOTE.xls")
    var_excel_quote = xlrd.open_workbook(location_quote)
    template_quote = var_excel_quote.sheet_by_index(0)

    @classmethod
    def setUpClass(cls):
        #s = Service("C:/Users/jgarcia/PycharmProjects/SNTDProject/drivers/Chrome/114/chromedriver.exe")
        s = "C:/Users/jgarcia/PycharmProjects/SNTDProject/drivers/Edge/116/msedgedriver.exe"
        #cls.driver = webdriver.Chrome(service=s)
        cls.driver = webdriver.Edge(executable_path=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):

        database = Database()

        for cont_input in range(1, data_input):
            print("                                                                    ")
            print("                                                                    ")
            print("********************************** ITERACIÓN # ", cont_input,
                  "**********************************")
            driver = self.driver

            for for_ambiente in range(0, 1):
                var_ambiente = self.template_quote.cell_value(cont_input, for_ambiente)
                if var_ambiente == "TEST1":
                    driver.get("https://sntdtest.tekprovider.net:9444/TekFinauto/Autogestion/Acceso/Login")
                elif var_ambiente == "TEST2":
                    driver.get("https://sntdqa.tekprovider.net:9081/TekFinauto/Autogestion/Acceso/Login")
                elif var_ambiente == "UAT1":
                    driver.get("http://192.168.30.225:83/TekFinauto/Autogestion/Acceso/Login")
                elif var_ambiente == "UAT2":
                    driver.get("http://192.168.30.225:92/TekFinauto/Autogestion/Acceso/Login")
                elif var_ambiente == "PRE":
                    driver.get("https://gcscreditoautobo.pre.mx.corp/TekFinauto/autogestion/Acceso/Login")
                elif var_ambiente == "PROD":
                    driver.get("https://www.autocredit-santander.com.mx/TekFinauto/AUTOGESTION/authentication")
                elif var_ambiente == "DEV":
                    driver.get("http://192.168.30.80:92/tekfinauto/autogestion/acceso/login")
                else:
                    print("No seleccionaste un ambiente. Verifica tu configuración y selecciona el ambiente deseado")
                    driver.close()
                    driver.quit()
                print("AMBIENTE:", var_ambiente)

                for for_canal in range(1, 2):
                    # LOGIN
                    login = LoginPage(driver)
                    if self.template_quote.cell_value(cont_input, for_canal) == "AGENCIA":
                        login.enter_username("TBBT01")
                    elif self.template_quote.cell_value(cont_input, for_canal) == "SUCURSAL":
                        login.enter_username("TBBT02")
                    else:
                        print("Error con el usuario. Verifica la configuración")
                        driver.close()
                        driver.quit()
                    print("CANAL:", self.template_quote.cell_value(cont_input, for_canal))

                    login.enter_password("S1santan")
                    login.click_login()

                    # BÚSQUEDA
                    search = SearchPage(driver)
                    search.click_nvaCot()

                    # QUOTE - PRODUCTO
                    quote = QuotePage(driver)
                    time.sleep(2)
                    for for_branch in range(2,3):
                        quote.click_agencia()
                        quote.enter_agencia(self.template_quote.cell_value(cont_input, for_branch))
                        print("----------------- SECCIÓN PRODUCTO -----------------")
                        print("AGENCIA:", self.template_quote.cell_value(cont_input, for_branch))
                        for for_productofinanciero in range(3, 4):
                            if self.template_quote.cell_value(cont_input, for_productofinanciero) == "ARRENDAMIENTO":
                                quote.click_arrendamiento()
                            else:
                                quote.click_credito()
                            print("PRODUCTO FINANCIERO:",
                                  self.template_quote.cell_value(cont_input, for_productofinanciero))

                            for for_tipoporducto in range(4, 5):
                                if self.template_quote.cell_value(cont_input, for_tipoporducto) == "NUEVO":
                                    quote.click_tipon()
                                elif self.template_quote.cell_value(cont_input, for_tipoporducto) == "SEMINUEVO":
                                    quote.click_tipos()
                                else:
                                    quote.click_tipom()
                                print("TIPO DE PRODUCTO:", self.template_quote.cell_value(cont_input, for_tipoporducto))

                                for for_tipouso in range(5, 6):
                                    if self.template_quote.cell_value(cont_input, for_canal) == "AGENCIA":
                                        if self.template_quote.cell_value(cont_input, for_tipouso) == "PARTICULAR":
                                            quote.click_uso_p()
                                        elif self.template_quote.cell_value(cont_input, for_tipouso) == "CHOFER PRVADO":
                                            quote.click_uso_cp()
                                        else:
                                            quote.click_uso_c()
                                    else:
                                        quote.click_uso_p()
                                    print("TIPO USO:", self.template_quote.cell_value(cont_input, for_tipouso))

                                    for for_tipopersona in range(6, 7):
                                        if self.template_quote.cell_value(cont_input, for_tipopersona) == "FISICA AE":
                                            time.sleep(1)
                                            quote.click_persona_fae()
                                        else:
                                            time.sleep(1)
                                            quote.click_persona_f()
                                        print("TIPO PERSONA:",
                                              self.template_quote.cell_value(cont_input, for_tipopersona))

                                        time.sleep(1)
                                        quote.click_marca()

                                        if self.template_quote.cell_value(cont_input,for_productofinanciero) == "ARRENDAMIENTO":
                                            if self.template_quote.cell_value(cont_input, for_tipoporducto) == "MOTO":
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
                                                time.sleep(1)
                                                if self.template_quote.cell_value(cont_input,for_tipoporducto) == "SEMINUEVO":
                                                    quote.click_monto_vehiculo()
                                                    time.sleep(1)
                                                    quote.clear_monto_vehiculo()
                                                    time.sleep(1)
                                                    quote.enter_monto_vehiculo("$510,900.00")
                                        else:
                                            if self.template_quote.cell_value(cont_input, for_tipoporducto) == "MOTO":
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
                                                quote.enter_marca("MAZDA")
                                                time.sleep(1)
                                                quote.click_modelo()
                                                quote.enter_modelo("MAZDA CX-3")
                                                time.sleep(1)
                                                quote.click_version()
                                                quote.enter_version("MAZDA CX-3 I 2WD")
                                                time.sleep(1)
                                                quote.click_ano()
                                                quote.enter_ano_down1()
                                                time.sleep(1)
                                                quote.enter_ano()
                                                time.sleep(1)
                                                if self.template_quote.cell_value(cont_input,for_tipoporducto) == "SEMINUEVO":
                                                    quote.click_monto_vehiculo()
                                                    time.sleep(1)
                                                    quote.clear_monto_vehiculo()
                                                    time.sleep(1)
                                                    quote.enter_monto_vehiculo("$510,900.00")

                                    for for_tipocredito in range(7, 8):
                                        print("TIPO CRÉDITO:",self.template_quote.cell_value(cont_input, for_tipocredito))
                                        print("---------- SECCIÓN PLAN DE FINANCIAMIENTO ----------")
                                        for for_plan in range(8, 9):
                                            if self.template_quote.cell_value(cont_input,for_productofinanciero) == "ARRENDAMIENTO":
                                                quote.click_plan("AUTOMATION ARRENDAMIENTO")
                                            else:
                                                quote.click_plan(self.template_quote.cell_value(cont_input, for_plan))
                                                print("PLAN:", self.template_quote.cell_value(cont_input, for_plan))

                                            time.sleep(2)

                                            for for_acce in range(9, 10):
                                                if self.template_quote.cell_value(cont_input, for_acce) == "SI":
                                                    print("***** CUENTA CON ACCESORIOS *****")
                                                    quote.click_accesorios("Accesorios Vehículo")
                                                    time.sleep(1)
                                                    quote.click_descripcion_accesorios("GPS")
                                                    for for_monto_acce in range(10, 11):
                                                        time.sleep(1)
                                                        quote.click_monto_accesorios(self.template_quote.cell_value(cont_input, for_monto_acce))
                                                        print("MONTO ACCESORIOS:", self.template_quote.cell_value(cont_input, for_monto_acce))
                                                        for for_type_acce in range(11, 12):
                                                            time.sleep(1)
                                                            quote.click_accesorios_type(self.template_quote.cell_value(cont_input,for_type_acce))
                                                            print("FORMA DE PAGO:",self.template_quote.cell_value(cont_input,for_type_acce))
                                                else:
                                                    quote.click_garantia()

                                                quote.click_cuotas_show()
                                                time.sleep(4)
                                                for for_plazo in range(12, 13):
                                                    print("PLAZO:",int(self.template_quote.cell_value(cont_input,for_plazo)))
                                                    cuota_ = "{}{}".format("divTermContent_",int(self.template_quote.cell_value(cont_input,for_plazo)))
                                                    str_monto = str(cuota_)
                                                    self.driver.find_element(By.ID, str_monto).click()

                                                    time.sleep(1)
                                                    for for_ge in range(13,14):
                                                        print("GARANTÍA EXTENDIDAE:",self.template_quote.cell_value(cont_input, for_ge))
                                                        if self.template_quote.cell_value(cont_input, for_ge) == "SI":
                                                            time.sleep(2)
                                                            quote.click_GE()
                                                        else:
                                                            quote.click_label()
                                                        for for_sra in range(14, 15):
                                                            print("SEGURO ROBO DE AUTOPARTES:",self.template_quote.cell_value(cont_input, for_sra))
                                                            if self.template_quote.cell_value(cont_input,for_sra) == "SI":
                                                                quote.click_SRA()
                                                            else:
                                                                quote.click_label()
                                                            for for_gap in range(15, 16):
                                                                print("GARANTÍA EXTENDIDAE:",self.template_quote.cell_value(cont_input,for_gap))
                                                                if self.template_quote.cell_value(cont_input,for_gap) == "SI":
                                                                    quote.click_GaP()
                                                                    time.sleep(1)
                                                                else:
                                                                    quote.click_aceptar_msj_gap()
                                                                    time.sleep(1)
                                                            quote.click_aceptar_msj_gap()
                                                            driver.execute_script('window.scrollBy(0, 500);')

                                                            print("------------------ SEGURO DE AUTO ------------------")
                                                            for for_insurance in range(16,17):
                                                                print("SEGURO DE DAÑOS:",self.template_quote.cell_value(cont_input,for_insurance))



                                                    time.sleep(3)

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

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
        cls.driver.quit()
        print("Test complete")


if __name__ == '__main__':
    unittest.main()
