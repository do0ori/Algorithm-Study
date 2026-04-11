import unittest

from 참가할_대회_고르기 import solution


class TestProblem2(unittest.TestCase):
    def test_examples(self):
        contests = [[1, 5, 2, 3], [9, 9, 9, 9], [1, 9, 3, 9], [4, 3, 2, 1]]
        self.assertEqual(solution(contests, 2, 4), [0, 3])
        self.assertEqual(solution(contests, 3, 4), [0, 2, 3])
        self.assertEqual(solution(contests, 4, 4), [0, 1, 2, 3])

    def test_tie_break(self):
        contests = [[1, 1, 1], [2, 2, 2], [1, 1, 1]]
        self.assertEqual(solution(contests, 2, 2), [0, 1])

    def test_single_pick(self):
        contests = [[5, 5], [1, 2], [2, 2]]
        self.assertEqual(solution(contests, 1, 2), [1])


if __name__ == "__main__":
    unittest.main()
