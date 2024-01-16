import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

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

        if C53 > 0:
            tir = (1 + np.irr(cotizador_data)) ** C54 - 1
        else:
            tir = 0

        # Resultado
        print(f"La TIR calculada es: {tir * 100:.2f}%")

if __name__ == '__main__':
    unittest.main()
