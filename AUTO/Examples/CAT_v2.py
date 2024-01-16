import numpy_financial as npf
C53 = 36
C54 = 12

# Datos de Cotizador!BI34:BI107
cotizador_data = [
    -318225.0862, 946.7681956, 13802.94467, 13802.94467, 13802.94467,
    13802.94467, 13802.94467, 13802.94467, 13802.94467, 13802.94467,
    13802.94467, 13802.94467, 13802.94467, 13802.94467, 13802.94467,
    13802.94467, 13802.94467, 13802.94467, 13802.94467, 13802.94467,
    13802.94467, 13802.94467, 13802.94467, 13802.94467, 13802.94467,
    13802.94467, 13802.94467, 13802.94467, 13802.94467, 13802.94467,
    13802.94467, 13802.94467, 13802.94467, 13802.94467, 13802.94467,
]

# Cálculo de la TIR utilizando numpy-financial
if C53 > 0:
    cash_flows = [0] + cotizador_data
    tir = (1 + npf.irr(cash_flows)) ** C54 - 1
else:
    tir = 0

# Resultado
print(f"La TIR calculada es: {tir * 100:.2f}%")