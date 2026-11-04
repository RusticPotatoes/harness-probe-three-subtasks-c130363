import unittest

from shipping.stats import chunked_parcel


class Behaviour(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(chunked_parcel(*([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1)), [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]])


if __name__ == "__main__":
    unittest.main()
