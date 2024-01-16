import unittest
import openpyxl
import xlrd
import json
from datetime import datetime

class MyTestCase(unittest.TestCase):

    archivo_excel = xlrd.open_workbook('C:/Automation_Performance_Sast/SNTD_QUOTE_PF.xls')
    hoja = archivo_excel.sheet_by_index(0)

    for numero_fila in range(1, hoja.nrows):
        fila = {
            "var_ambiente": hoja.cell_value(numero_fila, 0),
            "var_canal": hoja.cell_value(numero_fila, 1),
            "var_agencia": hoja.cell_value(numero_fila, 2),
            "var_tipo_producto": hoja.cell_value(numero_fila, 3),
            "var_tipo_uso": hoja.cell_value(numero_fila, 4),
            "var_tipo_persona": hoja.cell_value(numero_fila, 5),
            "var_plan": hoja.cell_value(numero_fila, 20),
            "var_accesorios": hoja.cell_value(numero_fila, 6),
            "var_monto_accesorios": hoja.cell_value(numero_fila, 7),
            "var_forma_pago_acce": hoja.cell_value(numero_fila, 8),
            "var_plazo": int(hoja.cell_value(numero_fila, 9)),
            "var_garantia_ext": hoja.cell_value(numero_fila, 10),
            "var_seguro_robo_aut": hoja.cell_value(numero_fila, 11),
            "var_gap": hoja.cell_value(numero_fila, 12),
            "var_seguro_danos": hoja.cell_value(numero_fila, 13),
            "var_forma_pago": hoja.cell_value(numero_fila, 14),
            "var_tipo": hoja.cell_value(numero_fila, 15),
            "var_cp": hoja.cell_value(numero_fila, 16),
            "var_cobertura": hoja.cell_value(numero_fila, 17),
            "var_fecha": hoja.cell_value(numero_fila, 18),
            "var_sexo": hoja.cell_value(numero_fila, 19),
            # Continúa con el resto de los valores
        }
        fila_json = json.dumps(fila)
        fecha_excel = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(fila["var_fecha"]) - 2)

        # for key, value in fila.items():
        #     print(key, ":", value)
        print("Fecha:", fecha_excel.strftime('%d/%m/%Y'))
        print(fila["var_cobertura"])
        print(fila["var_plan"])



if __name__ == '__main__':
    unittest.main()
