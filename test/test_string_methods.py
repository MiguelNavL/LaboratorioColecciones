"""
Algunos ejemplos de pruebas unitarias.

Sin embargo estas pruebas no están verificando algún modulo externo
sino están sirviendo para comprobar algunas aserciones usando las funciones
más comunes para trabajar con textos o algunos casos estáticos

La próxima vez estos comentarios también estarán en inglés

"""

import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_greater_than(self):
        # if you change a = 0 , then a is not greater than 0 and the test fails
        a = 3
        # check if a is greater than 1
        self.assertGreater(a, 1)

    def test_list_equals(self):
        # lets create two list with the same elements and check if both are equals
        list_one = [2, 9, 0, 1]
        list_two = [2, 9, 0, 1]  # if we change list_two = [2, 0, 9, 1] the test fails
        self.assertListEqual(list_one, list_two)


if __name__ == '__main__':
    unittest.main()
