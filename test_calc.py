import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    #passing case
    def test_add(self):
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)

    #passing case
    def test_subtract(self):
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)

    #passing case
    def test_multiply(self):
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)

    #Passing test case
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(8, 0)

    #Fixed test case
    def test_invalid_addition(self):
        with self.assertRaises(TypeError):
            self.calc.add(3, '5')
    
    #Fixed test case
    def test_invalid_substractor(self):
        with self.assertRaises(TypeError):
            self.calc.subtract(4, "5")   

if __name__ == '__main__':
    unittest.main()
