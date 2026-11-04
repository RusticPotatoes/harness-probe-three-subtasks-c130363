import unittest

from shipping.pagination import shorten_receipt


class Behaviour(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(shorten_receipt(*('daaece ', 4)), 'd...')


if __name__ == "__main__":
    unittest.main()
