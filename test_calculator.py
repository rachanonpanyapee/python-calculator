import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_sub2(self):
        self.assertEqual(self.calc.subtract(5, -5), 10)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_mul2(self):
        self.assertEqual(self.calc.multiply((-2), 3), (-6))

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(-10, 4), -2)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_mod2(self):
        self.assertEqual(self.calc.modulo(-3, -3), 0)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()