# coding: utf-8
#全体の設計
#Stack  pop push
#文字列を空白区切りで入力してけいさんけっk
# 普通は add, sub, mul, div かな（by 内田）
# func(str) = ans
#ex. 2 3 +

import unittest
import rpn

class TestRPN(unittest.TestCase):
    def test_calc_add(self):
        self.assertEqual(5,   rpn.calc("2 3 +"))
        self.assertEqual(9,   rpn.calc("2 3 4 + +"))
        self.assertEqual(10,  rpn.calc("2 3 + 5 +"))
        self.assertEqual(3,   rpn.calc("2 3 + 3"))
        self.assertEqual(3,   rpn.calc("5 2 -"))
        self.assertEqual(6,   rpn.calc("5 2 3 - -"))
        self.assertEqual(0,   rpn.calc("5 2 - 3 -"))
        self.assertEqual(7,   rpn.calc("5 2 - 4 +"))
        self.assertEqual(120, rpn.calc("5 2 3 * * 4 *"))
        self.assertEqual(8,   rpn.calc("32 4 2 / / 2 /"))
        self.assertEqual(5,   rpn.calc("5 6 + 1 - 2 * 4 /"))
        self.assertEqual(6.4,   rpn.calc("32 5 /"))
        self.assertEqual(10,   rpn.calc("32 3.2 /"))

    def test_num(self):
        self.assertTrue(rpn.num("2"))
        self.assertTrue(rpn.num("-2.3"))
        self.assertFalse(rpn.num("+"))
        # なぜpassを残しているのか
"""
    def test_add(self):
        #"1 2 +", 3
        pass

    def test_sub(self):
        pass

    def test_mul(self):
        pass

    def test_div(self):
        pass
"""

if __name__ == '__main__':
    unittest.main()


