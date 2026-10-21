import unittest
from main import calculate
class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(8, 2, "1"), 10)

if __name__ == "__main__":
    unittest.main()