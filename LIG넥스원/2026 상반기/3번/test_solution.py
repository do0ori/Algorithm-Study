import unittest

from 개미굴의_미정_통로_범위_찾기 import solution


class TestProblem3(unittest.TestCase):
    def test_examples(self):
        edges = [
            [1, 2, 3, 5],
            [2, 4, 2, 5],
            [3, 4, 3, 5],
            [4, 5, 1, 3],
            [3, 6, 4, 4],
            [4, 6, 0, 0],
            [5, 6, 0, 0],
        ]
        self.assertEqual(solution(6, edges, [3, 4, 5]), [3, 5])
        self.assertEqual(solution(6, edges, [4]), [1, 1])

        self.assertEqual(
            solution(2, [[1, 2, 7, 11], [1, 2, 0, 0]], [4, 7, 8, 9, 10, 11]),
            [4, 4],
        )
        self.assertEqual(
            solution(2, [[1, 2, 2, 2], [1, 2, 4, 4], [1, 2, 0, 0]], [2, 4]),
            [1, 1],
        )

    def test_additional_case(self):
        edges = [[1, 2, 1, 2], [2, 3, 0, 0]]
        self.assertEqual(solution(3, edges, [1, 2]), [1, 2])


if __name__ == "__main__":
    unittest.main()
