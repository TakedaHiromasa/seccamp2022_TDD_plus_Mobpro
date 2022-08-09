import unittest

"""
- ランダムに数字を生成する関数
- 数字を受け取る関数
- 正誤判定する関数
"""

class TestJudge(unittest.TestCase):
    def setUp(self):
        self.numberGuess = NumberGuess(3)

    def test_judgement_correct(self):
        self.assertEqual(self.numberGuess.judgement(3), 'correct')

    def test_judgement_smaller(self):
        self.assertEqual(self.numberGuess.judgement(1), 'smaller')
        self.assertEqual(self.numberGuess.judgement(2), 'smaller')

    def test_judgement_greater(self):
        self.assertEqual(self.numberGuess.judgement(4), 'greater')
        self.assertEqual(self.numberGuess.judgement(100), 'greater')
        self.assertEqual(self.numberGuess.judgement(10 ** 100), 'greater')

    def test_judgement_invalid(self):
        self.assertEqual(self.numberGuess.judgement(-1), 'invalid')
        self.assertEqual(self.numberGuess.judgement("a"), 'invalid')
        self.assertEqual(self.numberGuess.judgement(1.1), 'invalid')
        self.assertEqual(self.numberGuess.judgement("百"), 'invalid')
        self.assertEqual(self.numberGuess.judgement("100"), 'invalid')
        self.assertEqual(self.numberGuess.judgement(None), 'invalid')

class TestNumberGuess(unittest.TestCase):
    

