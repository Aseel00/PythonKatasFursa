import unittest
from katas.stock_trader_v2 import max_profit  # Replace with actual module name

class TestMaxProfitMultipleTransactions(unittest.TestCase):

    def test_empty_prices(self):
        self.assertEqual(max_profit([]), 0)

    def test_single_price(self):
        self.assertEqual(max_profit([10]), 0)

    def test_all_same_prices(self):
        self.assertEqual(max_profit([5, 5, 5, 5]), 0)

    def test_alternating_prices(self):
        self.assertEqual(max_profit([1, 3, 2, 5, 4, 7]), 8)  #


