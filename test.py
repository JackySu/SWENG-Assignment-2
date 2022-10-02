from calc import *
import unittest

class TestCases(unittest.TestCase):

    def test_split_expression(self):
        try:
            self.assertEqual(split_num_operators("11+22-33*44/55"), ["11", "+", "22", "-", "33", "*", "44", "/", "55"])
        except Exception as e:
            print(e)

    def test_evaluate(self):
        try:
            self.assertEqual(main(s="1+2*3-4/5"), 6.2)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
