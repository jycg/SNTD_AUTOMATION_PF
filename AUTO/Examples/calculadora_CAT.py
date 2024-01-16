import unittest

class MyTestCase(unittest.TestCase):

    monto = 10000
    accesorios = 500
    garantia = 1000
    seguro_vida = 200
    seguro_danios = 300
    comision = 500
    tasa_interes = 0.10
    plazo_meses = 12
    obligatorios = [seguro_vida, seguro_danios]  # Puedes agregar los cargos obligatorios en una lista

    def test_something(monto, accesorios, garantia, seguro_vida, seguro_danios, comision, tasa_interes, plazo_meses, obligatorios):

        # Calcula la suma de los cargos adicionales
        cargos_adicionales = accesorios + garantia + sum(obligatorios) + comision

        # Calcula el monto total a pagar
        monto_total = monto + cargos_adicionales

        # Calcula la Tasa de Interés Real (TIR)
        tir = (1 + tasa_interes / 12) ** plazo_meses - 1

        # Calcula el CAT
        iva = cargos_adicionales * 0.16
        monto_total_iva = monto_total + iva
        cat = ((monto_total_iva / monto) ** (1 / plazo_meses) - 1) * (365 / plazo_meses) * 100

        return cat

        #CAT = MyTestCase.test_something(monto, accesorios, garantia, seguro_vida, seguro_danios, comision, tasa_interes, plazo_meses,obligatorios)

        CAT = test_something(self, monto, accesorios, garantia, seguro_vida, seguro_danios, comision, tasa_interes, plazo_meses,obligatorios)

        print("El CAT es:", CAT)

if __name__ == '__main__':
    unittest.main()
