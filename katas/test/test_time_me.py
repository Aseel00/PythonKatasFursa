import time
import unittest
from katas.time_me import measure_execution_time


def fast_fun():
    return 0
def slow_fun():
    time.sleep(2)
class TestTimeMe(unittest.TestCase):

    def test_time_me_1(self):
        self.assertLess(measure_execution_time(fast_fun),0.5)
    def test_time_me_2(self):
        self.assertGreaterEqual(measure_execution_time(slow_fun),2)