import unittest
import xlrd

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

if __name__ == '__main__':
    unittest.main()
