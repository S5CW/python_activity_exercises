import unittest

from InvestIn Exercises import solution2


class Level2TestCase(unittest.TestCase):

    def test_level2isOdd(self):
        self.assertEqual(solution2(3), 'Weird')

    def test_level2isNotOdd(self):
        self.assertEqual(solution2(4), 'Not Weird')

    def test_level2isEveninRangeNotWeird(self):
        self.assertEqual(solution2(2), 'Not Weird')

    def test_level2isNotEveninRangeNotWeird(self):
        self.assertEqual(solution2(5), 'Weird')

    def test_level2isEveninRangeWeird(self):
        self.assertEqual(solution2(8), 'Weird')

    def test_level2isNotEveninRangeWeird(self):
        self.assertEqual(solution2(15), 'Weird')

    def test_level2isEveninRangeGreaterThan20(self):
        self.assertEqual(solution2(22), 'Not Weird')

    def test_level2isNotEveninRangeGreaterThan20(self):
        self.assertEqual(solution2(23), 'Weird')

    def test_level2isEveninRangeGreaterThan100(self):
        self.assertEqual(solution2(102), None)


if __name__ == '__main__':
    unittest.main()
