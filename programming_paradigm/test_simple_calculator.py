import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # -------- Addition Tests --------
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)       # normal positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)      # negative + positive
        self.assertEqual(self.calc.add(-5, -5), -10)   # negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)       # zero case
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)  # float addition

    # -------- Subtraction Tests --------
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # -------- Multiplication Tests --------
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)

    # -------- Division Tests --------
    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
