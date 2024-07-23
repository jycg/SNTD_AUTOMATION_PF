from AUTO.Locator.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class QuotePage:
    def __init__(self, driver):
        self.driver = driver

    # PRODUCTO
    def click_agencia(self):
        try:
            agencia_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locators.agencia_click))
            )
            agencia_element.click()
        except Exception as e:
            print(f"Error al hacer clic en agencia: {e}")

    def enter_agencia(self, agencia):
        try:
            agencia_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locators.agencia_enter))
            )
            agencia_input.send_keys(agencia, Keys.ENTER)
        except Exception as e:
            print(f"Error al ingresar agencia: {e}")

    def click_arrendamiento(self):
        self.driver.find_element(By.ID, Locators.producto_arrendamiento).click()
        # try:
        #     arrendamiento_element = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.ID, Locators.producto_arrendamiento))
        #     )
        #     arrendamiento_element.click()
        # except Exception as e:
        #     print(f"Error al hacer clic en arrendamiento: {e}")

    def click_tipon(self):
        self.driver.find_element(By.XPATH, Locators.producto_tipo_n).click()

    def click_tipon_BYD(self):
        self.driver.find_element(By.XPATH, Locators.producto_tipo_n_BYD).click()

    def click_tipon_OM(self):
        self.driver.find_element(By.XPATH, Locators.producto_tipo_n_OM).click()

    def click_tipos(self):
        self.driver.find_element(By.XPATH, Locators.producto_tipo_s).click()

    def click_tipos_OM(self):
        self.driver.find_element(By.XPATH, Locators.producto_tipo_s_OM).click()

    def click_tipom(self):
        self.driver.find_element(By.XPATH, Locators.producto_tipo_m).click()

    def click_tipom_OM(self):
        self.driver.find_element(By.XPATH, Locators.producto_tipo_m_OM).click()

    def click_uso_p(self):
        self.driver.find_element(By.XPATH, Locators.producto_uso_p).click()

    def click_uso_p_BYD(self):
        self.driver.find_element(By.XPATH, Locators.producto_uso_p_BYD).click()

    def click_uso_cp(self):
        self.driver.find_element(By.ID, Locators.producto_uso_cp).click()

    def click_uso_c(self):
        self.driver.find_element(By.ID, Locators.producto_uso_c).click()

    def click_p_f(self):
        self.driver.find_element(By.XPATH, Locators.producto_p_f).click()

    def click_p_f_BYD(self):
        self.driver.find_element(By.XPATH, Locators.producto_p_f_BYD).click()

    def click_p_f_OM(self):
        self.driver.find_element(By.XPATH, Locators.producto_p_f_OM).click()

    def click_p_fae(self):
        self.driver.find_element(By.XPATH, Locators.producto_p_fae).click()

    def click_p_fae_BYD(self):
        self.driver.find_element(By.XPATH, Locators.producto_p_fae_BYD).click()

    def click_p_fae_OM(self):
        self.driver.find_element(By.XPATH, Locators.producto_p_fae_OM).click()

    def click_marca(self):
        self.driver.find_element(By.ID, Locators.producto_marca_click).click()

    def enter_marca(self, marca):
        self.driver.find_element(By.XPATH, Locators.producto_marca_enter).send_keys(marca, Keys.ENTER)

    def click_modelo(self):
        self.driver.find_element(By.ID, Locators.producto_modelo_click).click()

    def enter_modelo(self, modelo):
        self.driver.find_element(By.XPATH, Locators.producto_modelo_enter).send_keys(modelo, Keys.ENTER)

    def click_version(self):
        self.driver.find_element(By.ID, Locators.producto_version_click).click()

    def enter_version(self, version):
        self.driver.find_element(By.XPATH, Locators.producto_version_enter).send_keys(version, Keys.ENTER)

    def click_ano(self):
        self.driver.find_element(By.ID, Locators.producto_ano_click).click()

    def enter_anio(self, anio):
        self.driver.find_element(By.XPATH, Locators.producto_anio_enter).send_keys(anio, Keys.ENTER)

    def click_section_divListPrice(self):
        self.driver.find_element(By.ID, Locators.producto_section_divListPrice).click()

    def click_monto_vehiculo(self):
        self.driver.find_element(By.ID, Locators.producto_monto_vehiculo).click()

    def clear_monto_vehiculo(self):
        self.driver.find_element(By.ID, Locators.producto_monto_vehiculo).send_keys(Keys.CLEAR)

    def control_monto_vehiculo(self):
        self.driver.find_element(By.ID, Locators.producto_monto_vehiculo).send_keys(Keys.CONTROL + "A")

    def enter_monto_vehiculo(self, monto_v):
        self.driver.find_element(By.ID, Locators.producto_monto_vehiculo).send_keys(monto_v, Keys.ENTER)

    # PLAN
    def click_plan(self, plan):
        select = Select(self.driver.find_element(By.ID, Locators.plan_plan))
        select.select_by_visible_text(plan)

    def click_accesorios(self, accesorios):
        self.driver.find_element(By.ID, Locators.plan_accesorios).send_keys(accesorios)

    def click_descripcion_accesorios(self, desc_acce):
        self.driver.find_element(By.ID, Locators.plan_desc_accesorios).send_keys(desc_acce)

    def click_monto_accesorios(self, monto_acce):
        self.driver.find_element(By.ID, Locators.plan_monto_accesorios).send_keys(Keys.CONTROL + "A")
        self.driver.find_element(By.ID, Locators.plan_monto_accesorios).send_keys(Keys.CLEAR)
        self.driver.find_element(By.ID, Locators.plan_monto_accesorios).send_keys(monto_acce)

    def click_accesorios_type(self, typeacce):
        self.driver.find_element(By.XPATH, Locators.plan_type_accesories).send_keys(typeacce)

    def click_garantia(self):
        self.driver.find_element(By.ID, Locators.plan_g_ext).click()

    def click_garantia_select(self):
        self.driver.find_element(By.ID, Locators.plan_g_ext).send_keys(Keys.DOWN)
        self.driver.find_element(By.ID, Locators.plan_g_ext).send_keys(Keys.ENTER)

    def click_monto_garantia(self, monto_garantia):
        self.driver.find_element(By.ID, Locators.plan_g_ext_monto).send_keys(Keys.CLEAR)
        self.driver.find_element(By.ID, Locators.plan_g_ext_monto).send_keys(Keys.LEFT)
        self.driver.find_element(By.ID, Locators.plan_g_ext_monto).send_keys(Keys.LEFT)
        self.driver.find_element(By.ID, Locators.plan_g_ext_monto).send_keys(Keys.LEFT)
        self.driver.find_element(By.ID, Locators.plan_g_ext_monto).send_keys(Keys.LEFT)
        self.driver.find_element(By.ID, Locators.plan_g_ext_monto).send_keys(monto_garantia)

    def click_garantia_type(self, typegarantia):
        self.driver.find_element(By.ID, Locators.plan_g_ext_forma_pago).send_keys(typegarantia)

    def click_cuotas_show(self):
        self.driver.find_element(By.ID, Locators.plan_cuotas_show).click()

    def click_cuotas_select(self):
        self.driver.find_element(By.ID, Locators.plan_cuotas_select).click()

    def click_GE(self):
        self.driver.find_element(By.NAME, Locators.plan_garantia_extendida).click()

    def click_SRA_Advanced(self):
        self.driver.find_element(By.XPATH, Locators.plan_seguro_robo_advanced).click()

    def click_SRA_Signature(self):
        self.driver.find_element(By.XPATH, Locators.plan_seguro_robo_signature).click()

    def click_GaP(self):
        self.driver.find_element(By.ID, Locators.plan_seguro_gap).click()

    def click_GaP_type(self, typegapformapago):
        self.driver.find_element(By.ID, Locators.plan_seguro_gap_forma_pago).send_keys(typegapformapago)

    def click_label(self):
        self.driver.find_element(By.XPATH, Locators.alert_label).click()

    def click_coberturas(self):
        self.driver.find_element(By.ID, Locators.plan_coberturas).click()

    def click_aceptar_msj_gap(self):
        self.driver.find_element(By.XPATH, Locators.plan_aceptar_click).click()

    # SEGURO
    def click_insurance_no(self):
        self.driver.find_element(By.ID, Locators.insurance_no).click()

    def click_insurance_si(self):
        self.driver.find_element(By.ID, Locators.insurance_si).click()

    def click_insurance_manual(self):
        self.driver.find_element(By.ID, Locators.insurance_prima_manual).click()

    def click_msj_aceptar(self):
        self.driver.find_element(By.XPATH, Locators.insurance_msj_aceptar_click).click()

    def click_insurance_formapago(self):
        self.driver.find_element(By.ID, Locators.insurance_formapago).click()

    def enter_insurance_formapago(self, formapago):
        self.driver.find_element(By.ID, Locators.insurance_formapago).send_keys(formapago)

    def click_insurance_tipo(self):
        self.driver.find_element(By.ID, Locators.insurance_tipo).click()

    def enter_insurance_tipo(self, tipo):
        self.driver.find_element(By.ID, Locators.insurance_tipo).send_keys(tipo)

    def click_insurance_cp(self):
        self.driver.find_element(By.ID, Locators.insurance_cp).click()

    def clear_insurance_cp(self):
        self.driver.find_element(By.ID, Locators.insurance_cp).clear()

    def enter_insurance_cp(self, cp):
        self.driver.find_element(By.ID, Locators.insurance_cp).send_keys(cp)

    def click_insurance_cobertura(self):
        self.driver.find_element(By.ID, Locators.insurance_cobertura).click()

    def enter_insurance_cobertura(self, cobertura):
        self.driver.find_element(By.ID, Locators.insurance_cobertura).send_keys(cobertura)

    def click_insurance_birthdate(self):
        self.driver.find_element(By.ID, Locators.insurance_birthdate).click()

    def clear_insurance_birthdate(self):
        self.driver.find_element(By.ID, Locators.insurance_birthdate).clear()

    def enter_insurance_birthdate(self, birthdate):
        self.driver.find_element(By.ID, Locators.insurance_birthdate).send_keys(birthdate)

    def click_insurance_male(self):
        self.driver.find_element(By.XPATH, Locators.insurance_male).click()

    def click_insurance_female(self):
        self.driver.find_element(By.XPATH, Locators.insurance_female).click()

    def click_insurance_msj_quote(self):
        self.driver.find_element(By.ID, Locators.insurance_btn_click).click()

    def click_insurance_recibo1(self):
        self.driver.find_element(By.ID, Locators.insurance_recibo1).click()

    def control_insurance_recibo1(self):
        self.driver.find_element(By.ID, Locators.insurance_recibo1).send_keys(Keys.CONTROL + "A")

    def clear_insurance_recibo1(self):
        self.driver.find_element(By.ID, Locators.insurance_recibo1).clear()

    def enter_insurance_recibo1(self, recibo1):
        self.driver.find_element(By.ID, Locators.insurance_recibo1).send_keys(recibo1)

    def click_insurance_recibo2(self):
        self.driver.find_element(By.ID, Locators.insurance_recibo2).click()

    def control_insurance_recibo2(self):
        self.driver.find_element(By.ID, Locators.insurance_recibo2).send_keys(Keys.CONTROL + "A")

    def clear_insurance_recibo2(self):
        self.driver.find_element(By.ID, Locators.insurance_recibo2).clear()

    def enter_insurance_recibo2(self, recibo2):
        self.driver.find_element(By.ID, Locators.insurance_recibo2).send_keys(recibo2)

    def click_insurance_subsecuente(self):
        self.driver.find_element(By.ID, Locators.insurance_subsecuente).click()

    def clear_insurance_subsecuente(self):
        self.driver.find_element(By.ID, Locators.insurance_subsecuente).clear()

    def enter_insurance_subsecuente(self, subsecuente):
        self.driver.find_element(By.ID, Locators.insurance_subsecuente).send_keys(subsecuente)

    def click_insurance_div(self):
        self.driver.find_element(By.ID, Locators.insurance_div).click()

    def click_insurance_insurance(self):
        self.driver.find_element(By.XPATH, Locators.insurance_insurance).click()

    def click_insurance_autocompara_si(self):
        self.driver.find_element(By.XPATH, Locators.insurance_autocompara_si).click()

    def click_insurance_autocompara_no(self):
        self.driver.find_element(By.XPATH, Locators.insurance_autocompara_no).click()

    def select_insurance_agencia(self, insuranceagencia):
        self.driver.find_element(By.ID, Locators.insurance_aseguradoras).send_keys(insuranceagencia)

    def select_insurance_UDI(self, udi):
        self.driver.find_element(By.ID, Locators.insurance_UDI).send_keys(udi)

    # INFORMACIÓN CLIENTE
    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def enter_fname(self, fname):
        self.driver.find_element(By.ID, Locators.information_fname).clear()
        self.driver.find_element(By.ID, Locators.information_fname).send_keys(fname)

    def enter_sname(self, sname):
        self.driver.find_element(By.ID, Locators.information_sname).clear()
        self.driver.find_element(By.ID, Locators.information_sname).send_keys(sname)

    def enter_flastname(self, flastname):
        self.driver.find_element(By.ID, Locators.information_flastname).clear()
        self.driver.find_element(By.ID, Locators.information_flastname).send_keys(flastname)

    def enter_slastname(self, slastname):
        self.driver.find_element(By.ID, Locators.information_slastname).clear()
        self.driver.find_element(By.ID, Locators.information_slastname).send_keys(slastname)

    def enter_lada(self, lada):
        self.driver.find_element(By.ID, Locators.information_lada).clear()
        self.driver.find_element(By.ID, Locators.information_lada).send_keys(lada)

    def enter_phone(self, phone):
        self.driver.find_element(By.ID, Locators.information_phone).clear()
        self.driver.find_element(By.ID, Locators.information_phone).send_keys(phone)

    def enter_cellphone(self, cellphone):
        self.driver.find_element(By.ID, Locators.information_cellphone).clear()
        self.driver.find_element(By.ID, Locators.information_cellphone).send_keys(Keys.CONTROL + "A")
        self.driver.find_element(By.ID, Locators.information_cellphone).send_keys(cellphone)

    def click_cellcompany(self, cellcompany):
        select_cellcompany = Select(self.driver.find_element(By.ID, Locators.information_cellcompany_click))
        select_cellcompany.select_by_visible_text(cellcompany)

    def enter_email(self, email):
        self.driver.find_element(By.ID, Locators.information_email).clear()
        self.driver.find_element(By.ID, Locators.information_email).send_keys(email)

    # QUOTE
    def click_aviso_1(self):
        self.driver.find_element(By.XPATH, Locators.quote_check_aviso_click_1).click()

    def click_aviso_2(self):
        self.driver.find_element(By.XPATH, Locators.quote_check_aviso_click_2).click()

    def click_aviso_msj(self):
        self.driver.find_element(By.XPATH, Locators.quote_check_aviso_msj_click).click()

    def click_imprimir(self):
        self.driver.find_element(By.ID, Locators.quote_imprimir_click).click()

    def click_solicita_credito(self):
        self.driver.find_element(By.ID, Locators.quote_solicita_credito).click()

    def click_si_confirm(self):
        self.driver.find_element(By.ID, Locators.quote_btnConfirmData).click()

    def get_code(self):
        self.driver.find_element(By.ID, Locators.quote_divCodigoVerTemp)

    def codigo_verificacion(self, codeverification):
        self.driver.find_element(By.ID, Locators.quote_txtConfirmCode).send_keys(Keys.CONTROL + "A")
        self.driver.find_element(By.ID, Locators.quote_txtConfirmCode).clear()
        self.driver.find_element(By.ID, Locators.quote_txtConfirmCode).send_keys(codeverification)

    def click_btnGotoCreditform(self):
        self.driver.find_element(By.ID, Locators.quote_btnGotoCreditform).click()
