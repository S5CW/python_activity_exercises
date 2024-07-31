import unittest

from InvestIn Exercises import solution1


class Level1TestCase(unittest.TestCase):

    def test_level1(self):
        self.assertEqual(solution1(), 'Hello World!')


if __name__ == '__main__':
    unittest.main()
