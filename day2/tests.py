import lisp
import unittest

class test_lisp(unittest.TestCase):
    calc = "(defun foo (a b) (+ a b))"
    def test_calc(self):
        env = lisp.Env
        self.assertEqual(3, lisp.eval("( + 1 2 )", env))
        self.assertEqual(3, lisp.eval("( defun foo ( a ) ( a ) ) ( foo 3 )", env))

if __name__ == '__main__':
    unittest.main()
