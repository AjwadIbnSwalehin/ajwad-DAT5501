import unittest
import numpy as np
from duration_calculator_script import compare_dates

# Assume your compare_dates function is defined in the module `date_comparison`
# from date_comparison import compare_dates

class TestCompareDates(unittest.TestCase):

    def test_future_date(self):
        future_date = (np.datetime64('today', 'D') + np.timedelta64(5, 'D')).astype(str)
        self.assertEqual(compare_dates(future_date), np.timedelta64(5, 'D'))

    def test_past_date(self):
        past_date = (np.datetime64('today', 'D') - np.timedelta64(10, 'D')).astype(str)
        self.assertEqual(compare_dates(past_date), np.timedelta64(10, 'D'))

    def test_today_date(self):
        today_date = np.datetime64('today', 'D').astype(str)
        self.assertEqual(compare_dates(today_date), np.timedelta64(0, 'D'))

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            compare_dates("2023-13-01")  # Invalid month
        with self.assertRaises(ValueError):
            compare_dates("2023-02-30")  # Invalid day

if __name__ == '__main__':
    unittest.main()