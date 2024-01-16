import unittest

import matplotlib.colors
import matplotlib.pyplot as pyplot
import xlrd
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt

# # Ejercicio 1
# n = [76, 24]
# p = n.copy()
# n.pop()
# print(p, n)

# labels = ('Python', 'Java', 'Scala', 'C#')
# sizes = [45, 30, 15, 10]
# # colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
# normdata = colors.Normalize(min(sizes), max(sizes))
# #colormap = cm.get_cmap("Blues")
# colormap = plt.get_cmap("Blues")
# colores = colormap(normdata(sizes))
#
# explode = (0.1, 0, 0, 0)
# pyplot.pie(sizes, explode=explode, labels=labels, autopct='%1.f%%', colors=colores, shadow=True, counterclock=False,
#            startangle=80)
# pyplot.show()

#archivo_excel = xlrd.open_workbook('C:/Automation_Performance_Sast/SNTD_QUOTE_PF.xls')
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
        "var_autocompara": hoja.cell_value(numero_fila, 26),
        "var_aseguradora": hoja.cell_value(numero_fila, 27),
        #"var_ejemplo": hoja.cell_value(numero_fila, 26),
        #"var_ejemplo2": hoja.cell_value(numero_fila, 27),
        # Continúa con el resto de los valores
    }
    print(fila)



if __name__ == '__main__':
    unittest.main()
