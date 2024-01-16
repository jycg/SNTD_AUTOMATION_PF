import unittest


class MyTestCaseSolicitud(unittest.TestCase):
    driver = None

    @classmethod
    def datos_personales(cls):
        print("Ejemplo")


if __name__ == '__main__':
    unittest.main()
