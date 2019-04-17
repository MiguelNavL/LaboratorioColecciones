import unittest
from LaboratorioColecciones.custom_functions.temperature_methods import *


class TestStringMethods(unittest.TestCase):

    def test_promedio_temperaturas(self):
        datos1 = {"a": 22, "b": 27, "c": 21, "d": 24, "e": 32}
        datos2 = {"a": 22, "b": 27}

        promedio1 = promedio_temperaturas(datos1)
        self.assertEqual(10.5, promedio1)

        promedio2 = promedio_temperaturas(datos2)
        self.assertEqual(4.083333333333333, promedio2)

    def test_mes_mas_caliente(self):
        datos = {"Enero": 22, "Marzo": 27, "Octubre": 21, "Diciembre": 24, "Junio": 32}

        resultado = mes_mas_caliente(datos)
        self.assertEqual("Junio", resultado[0])
        self.assertEqual(32, resultado[1])

    def test_promedio_tres_meses_mas_calientes(self):
        datos = {
            "Enero": 24,
            "Febrero": 22,
            "Marzo": 19,
            "Abril": 15,
            "Mayo": 20,
            "Junio": 22,
            "Julio": 25,
            "Agosto": 22,
            "Septiembre": 23,
            "Octubre": 24,
            "Noviembre": 28,
            "Diciembre": 29
        }

        resultado = promedio_tres_meses_mas_calientes(datos)
        self.assertEqual(27.333333333333332, resultado)


if __name__ == '__main__':
    unittest.main()
