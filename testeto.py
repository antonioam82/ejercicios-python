import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        #COMPRUEBA SI 'foo'.upper() == 'FOO'
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        #COMPRUEBA SI ES CIERTO QUE 'FOO' ESTÁ EN MAYUSCULAS
        self.assertTrue('FOO'.isupper())
        #COMPRUEBA SI ES FALSO QUE 'foo' ESTÁ EN MAYUSCULAS
        self.assertFalse('foo'.isupper())

    def test_split(self):
        s = 'hello world'
        #COMPRUEBA SI 's.split() == ['hello', 'world'].
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
