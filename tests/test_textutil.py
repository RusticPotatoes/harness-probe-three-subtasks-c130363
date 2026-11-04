import unittest

from shipping.textutil import distinct_ticket


class Behaviour(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(distinct_ticket(*('apple  PEAR  Fig  apple  pear  apple  pear  fig',)), 3)


if __name__ == "__main__":
    unittest.main()
