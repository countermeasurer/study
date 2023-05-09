import unittest
from lesson_014.bowling import get_score, WrongSymbol, SumError, get_score_europe


class MyBowlingTest(unittest.TestCase):

    def test_normal(self):
        result = get_score(get_string='-24/344-5/X-/71-/X')
        self.assertEqual(result, 121)

    def test_input_more_count_frames(self):
        with self.assertRaises(Exception):
            get_score(get_string='-24/344-5/X-/71-/X3')

    def test_input_wrong_sum_frame(self):
        with self.assertRaises(SumError):
            get_score(get_string='-48344-5/X-/71-/X1-')

    def test_input_errors(self):
        with self.assertRaises(Exception):
            get_score(get_string='-4/344-5/X-/71-/X1-')

    def test_input_less_count_frames(self):
        with self.assertRaises(Exception):
            get_score(get_string='-24/344-5/X-/71-/X3')

    def test_input_words(self):
        with self.assertRaises(Exception):
            get_score(get_string='-24/344-5/X-/71-/X3')

    def test_input_wrong_symbol(self):
        with self.assertRaises(WrongSymbol):
            get_score(get_string='-4.344-5/X-/71-/X1-')

    def test_europe_normal(self):
        result = get_score_europe(get_string='54X12636/1122112211')
        self.assertEqual(result, 59)

    def test_europe_input_more_count_frames(self):
        with self.assertRaises(Exception):
            get_score_europe(get_string='-24/344-5/X-/71-/X3')

    def test_europe_input_wrong_sum_frame(self):
        with self.assertRaises(SumError):
            get_score_europe(get_string='-48344-5/X-/71-/X1-')

    def test_europe_input_errors(self):
        with self.assertRaises(Exception):
            get_score_europe(get_string='-4/344-5/X-/71-/X1-')

    def test_europe_input_less_count_frames(self):
        with self.assertRaises(Exception):
            get_score_europe(get_string='-24/344-5/X-/71-/X3')

    def test_europe_input_words(self):
        with self.assertRaises(Exception):
            get_score_europe(get_string='-24/344-5/X-/71-/X3')

    def test_europe_input_wrong_symbol(self):
        with self.assertRaises(WrongSymbol):
            get_score_europe(get_string='-4.344-5/X-/71-/X1-')