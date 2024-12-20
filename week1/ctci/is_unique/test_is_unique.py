import unittest

from question_a import QuestionA
from question_b import QuestionB


class TestIsUnique(unittest.TestCase):
    cases = [("abcde", True), ("hello", False), ("apple", False), ("kite", True), ("paddle",False)];


    def test_question_a(self):
        for word, expected in self.cases:
            actual = QuestionA.is_unique(word)
            # print(f"{word}: expected: {expected} actual: {actual}")
            self.assertEqual(expected, actual)

    def test_question_b(self):
        for word, expected in self.cases:
            actual = QuestionB.is_unique(word)
            # print(f"{word}: expected: {expected} actual: {actual}")
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
