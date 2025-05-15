import unittest
from katas.stock_trader import max_profit  # replace with your actual module name

class TestMaxProfit(unittest.TestCase):


    def test_empty_list(self):
        self.assertEqual(max_profit([]), 0)

    def test_single_element(self):
        self.assertEqual(max_profit([10]), 0)

    def test_all_same_prices(self):
        self.assertEqual(max_profit([5, 5, 5, 5]), 0)

    def test_profit_at_start(self):
        self.assertEqual(max_profit([2, 10, 1, 3]), 8)

if __name__ == "__main__":
    unittest.main()
