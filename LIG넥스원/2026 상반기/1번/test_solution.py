import unittest

from 암호화된_잔고_복원 import solution


class TestProblem1(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution("55AA"), "551011")
        self.assertEqual(solution("55AB"), "55101")

    def test_additional_cases(self):
        self.assertEqual(solution("7A"), "77")
        self.assertEqual(solution("123B"), "1231")
        self.assertEqual(solution("9AA"), "9918")


if __name__ == "__main__":
    unittest.main()
