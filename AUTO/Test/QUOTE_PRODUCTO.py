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


def cotizador_producto(driver, fila, fila_environment):
    from AUTO.PageApp.quotePage import QuotePage
    import time
    try:
        quote = QuotePage(driver)
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

    except TimeoutException as e:
        error_message = f"Error en el escenario {fila['var_escenario']}: {str(e)}"
        logging.error(error_message)
        traceback.print_exc()
