import unittest

from InvestIn Exercises import solution9


class TestFindSecondLowestStudents(unittest.TestCase):
    def test_basic(self):
        records = [["chi", 20], ["beta", 50], ["alpha", 50]]
        result = solution9(records)
        self.assertEqual(result, ["alpha", "beta"])

    def test_all_same_scores(self):
        records = [["student1", 30], ["student2", 30], ["student3", 30]]
        result = solution9(records)
        self.assertEqual(result, [])

    def test_with_negative_and_positive_scores(self):
        records = [["anne", -2], ["greg", 3], ["joan", -2], ["peter", 1]]
        result = solution9(records)
        self.assertEqual(result, ["peter"])

    def test_empty_list(self):
        records = []
        result = solution9(records)
        self.assertEqual(result, [])

    def test_single_student(self):
        records = [["only", 42]]
        result = solution9(records)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
