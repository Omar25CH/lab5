import unittest
from division import dividir

class TestDividir(unittest.TestCase):

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(-10, 2), -5)
        self.assertEqual(dividir(-10, -2), 5)

    def test_dividir_entre_cero(self):
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()
    