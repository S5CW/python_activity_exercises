from __future__ import division

import unittest

from InvestIn Exercises import solution5


class Level5TestCase(unittest.TestCase):

    def test_level5_positive(self):
        result_list = solution5(3)
        expected_list = [0, 1, 4]

        self.assertEqual(result_list, expected_list)

    def test_level5_invalid(self):
        result_list = solution5(-1)
        self.assertEqual(result_list, [])


if __name__ == '__main__':
    unittest.main()
