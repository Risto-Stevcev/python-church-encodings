#!/usr/bin/env python
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from church import true, false, \
                   AND, OR, NOT, XOR, unchurch_bool, \
                   zero, one, two, three, num, unchurch_num, \
                   ifelse, \
                   is_zero, lt, leq, eq, geq, gt, \
                   succ, pred, add, sub, mult, div, exp, fac, \
                   cons, car, cdr, \
                   convertNZ, neg, onezero, unchurch_int, \
                   addZ, subZ, multZ, divZ



class TestChurch(unittest.TestCase):
    def test_true_false(self):
        self.assertTrue((true) (True)(False))
        self.assertEqual((true) (2.5)(3.2), 2.5)

        self.assertEqual((false) (True)(False), False)
        self.assertEqual((false) (5)(6), 6)

    def test_boolean_operators(self):
        self.assertTrue ((unchurch_bool) ((AND) (true)(true)))
        self.assertEqual((unchurch_bool) ((AND) (true)(false)), False)
        self.assertEqual((unchurch_bool) ((AND) (false)(true)), False)
        self.assertEqual((unchurch_bool) ((AND) (false)(false)), False)

        self.assertTrue ((unchurch_bool) ((OR) (true)(true)))
        self.assertTrue ((unchurch_bool) ((OR) (true)(false)))
        self.assertTrue ((unchurch_bool) ((OR) (false)(true)))
        self.assertEqual((unchurch_bool) ((OR) (false)(false)), False)

        self.assertEqual((unchurch_bool) ((NOT) (true)), False)
        self.assertTrue ((unchurch_bool) ((NOT) (false)))
        self.assertEqual((unchurch_bool) ((NOT) ((OR) (false)(true))), False)
        self.assertTrue ((unchurch_bool) ((NOT) ((XOR) (true)(true))))

        self.assertEqual((unchurch_bool) ((XOR) (true)(true)), False)
        self.assertTrue ((unchurch_bool) ((XOR) (true)(false)))
        self.assertTrue ((unchurch_bool) ((XOR) (false)(true)))
        self.assertEqual((unchurch_bool) ((XOR) (false)(false)), False)

    def test_natural_numbers(self):
        self.assertEqual((unchurch_num) (zero), 0)
        self.assertEqual((unchurch_num) (one), 1)
        self.assertEqual((unchurch_num) (two), 2)
        self.assertEqual((unchurch_num) (three), 3)

        self.assertEqual((unchurch_num) (num (12)), 12)
        self.assertEqual((unchurch_num) (num (17)), 17)
        self.assertEqual((unchurch_num) (num (950)), 950)

    def test_conditionals(self):
        self.assertEqual((unchurch_num) ((ifelse) (true)(one)(three)), 1)
        self.assertEqual((unchurch_num) ((ifelse) (false)(two)(three)), 3)

    def test_comparison_operators(self):
        self.assertTrue ((unchurch_bool) ((is_zero) (zero)))
        self.assertEqual((unchurch_bool) ((is_zero) (one)), False)

        self.assertEqual((unchurch_bool) ((lt) (zero)(zero)), False)
        self.assertEqual((unchurch_bool) ((lt) (num (7))(num (7))), False)
        self.assertEqual((unchurch_bool) ((lt) (num (14))(one)), False)
        self.assertTrue ((unchurch_bool) ((lt) (one)(two)))

        self.assertTrue ((unchurch_bool) ((leq) (zero)(zero)))
        self.assertTrue ((unchurch_bool) ((leq) (num (7))(num (7))))
        self.assertEqual((unchurch_bool) ((leq) (num (14))(one)), False)
        self.assertTrue ((unchurch_bool) ((leq) (one)(two)))

        self.assertTrue ((unchurch_bool) ((eq) (zero)(zero)))
        self.assertTrue ((unchurch_bool) ((eq) (num (7))(num (7))))
        self.assertEqual((unchurch_bool) ((eq) (num (14))(one)), False)
        self.assertEqual((unchurch_bool) ((eq) (one)(two)), False)

        self.assertTrue ((unchurch_bool) ((geq) (zero)(zero)))
        self.assertTrue ((unchurch_bool) ((geq) (num (7))(num (7))))
        self.assertTrue ((unchurch_bool) ((geq) (num (14))(one)))
        self.assertEqual((unchurch_bool) ((geq) (one)(two)), False)

        self.assertEqual((unchurch_bool) ((gt) (zero)(zero)), False)
        self.assertEqual((unchurch_bool) ((gt) (num (7))(num (7))), False)
        self.assertTrue ((unchurch_bool) ((gt) (num (14))(one)))
        self.assertEqual((unchurch_bool) ((gt) (one)(two)), False)

    def test_arithmetic_operators_N(self):
        self.assertEqual((unchurch_num) ((succ) (zero)), 1)
        self.assertEqual((unchurch_num) ((succ) (num (129))), 130)

        self.assertEqual((unchurch_num) ((pred) (zero)), 0)
        self.assertEqual((unchurch_num) ((pred) (one)), 0)
        self.assertEqual((unchurch_num) ((pred) (num (130))), 129)

        self.assertEqual((unchurch_num) ((add) (zero)(zero)), 0)
        self.assertEqual((unchurch_num) ((add) (zero)(one)), 1)
        self.assertEqual((unchurch_num) ((add) (three)(zero)), 3)
        self.assertEqual((unchurch_num) ((add) (num (77))(num (213))), 290)

        self.assertEqual((unchurch_num) ((sub) (zero)(zero)), 0)
        self.assertEqual((unchurch_num) ((sub) (zero)(one)), 0)
        self.assertEqual((unchurch_num) ((sub) (three)(zero)), 3)
        self.assertEqual((unchurch_num) ((sub) (num (213))(num (77))), 136)

        self.assertEqual((unchurch_num) ((mult) (zero)(zero)), 0)
        self.assertEqual((unchurch_num) ((mult) (three)(zero)), 0)
        self.assertEqual((unchurch_num) ((mult) (num (13))(num (99))), 1287)
        self.assertEqual((unchurch_num) ((mult) (one)(num (121))), 121)

        self.assertEqual((unchurch_num) ((div) (num (8)) (two)), 4)
        self.assertEqual((unchurch_num) ((div) (zero) (three)), 0)
        self.assertEqual((unchurch_num) ((div) (num (99)) (num (4))), 24)
        self.assertEqual((unchurch_num) ((div) (num (420)) (num (20))), 21)

        self.assertEqual((unchurch_num) ((exp) (zero) (zero)), 1)
        self.assertEqual((unchurch_num) ((exp) (zero) (three)), 0)
        self.assertEqual((unchurch_num) ((exp) (two) (num (8))), 256)
        self.assertEqual((unchurch_num) ((exp) (num (133)) (one)), 133)
     
        self.assertEqual((unchurch_num) ((fac) (zero)), 1)
        self.assertEqual((unchurch_num) ((fac) (one)), 1)
        self.assertEqual((unchurch_num) ((fac) (three)), 6)
        self.assertEqual((unchurch_num) ((fac) (num (5))), 120)
        self.assertEqual((unchurch_num) ((fac) (num (7))), 5040)

    def test_lists(self):
        clist = (cons) (num (4))((cons) (three)((cons) (two)((cons) (one)(true))))
        self.assertEqual((unchurch_num) ((car) (clist)), 4)
        self.assertEqual((unchurch_num) ((car) ((cdr) (clist))), 3)
        self.assertEqual((unchurch_num) ((car) ((cdr) ((cdr) (clist)))), 2)
        self.assertEqual((unchurch_num) ((car) ((cdr) ((cdr) ((cdr) (clist))))), 1)

    def test_integers(self):
        self.assertEqual((unchurch_int) ((convertNZ) (zero)), 0)
        self.assertEqual((unchurch_int) ((convertNZ) (three)), 3)
        self.assertEqual((unchurch_int) ((convertNZ) (num (45))), 45)
        self.assertEqual((unchurch_int) ((neg) ((convertNZ) (zero))), 0)
        self.assertEqual((unchurch_int) ((neg) ((convertNZ) (num (27)))), -27)

    def test_arithmetic_operators_Z(self):
        self.assertEqual((unchurch_int) ((addZ) ((convertNZ) (zero))
                                                ((convertNZ) (zero))), 0)
        self.assertEqual((unchurch_int) ((addZ) ((convertNZ) (zero))
                                                ((convertNZ) (one))), 1)
        self.assertEqual((unchurch_int) ((addZ) ((convertNZ) (three))
                                                ((convertNZ) (zero))), 3)
        self.assertEqual((unchurch_int) ((addZ) ((convertNZ) (num (77)))
                                         ((neg) ((convertNZ) (num (213))))), -136)

        self.assertEqual((unchurch_int) ((subZ) ((convertNZ) (zero))
                                                ((convertNZ) (zero))), 0)
        self.assertEqual((unchurch_int) ((subZ) ((convertNZ) (zero))
                                                ((convertNZ) (one))), -1)
        self.assertEqual((unchurch_int) ((subZ) ((neg) ((convertNZ) (num (14))))
                                                ((convertNZ) (num (99)))), -113)
        self.assertEqual((unchurch_int) ((subZ) ((convertNZ) (num (213)))
                                                ((convertNZ) (num (77)))), 136)
        self.assertEqual((unchurch_int) ((subZ) ((neg) ((convertNZ) (num (3))))
                                                ((neg) ((convertNZ) (num (99))))), 96)

        self.assertEqual((unchurch_int) ((multZ) ((convertNZ) (zero))
                                                 ((convertNZ) (zero))), 0)
        self.assertEqual((unchurch_int) ((multZ) ((convertNZ) (three))
                                                 ((convertNZ) (zero))), 0)
        self.assertEqual((unchurch_int) ((multZ) ((neg) ((convertNZ) (num (3))))
                                                 ((convertNZ) (num (99)))), -297)
        self.assertEqual((unchurch_int) ((multZ) ((neg) ((convertNZ) (one)))
                                                 ((neg) ((convertNZ) (num (121))))), 121)

        self.assertEqual((unchurch_int) ((divZ) ((convertNZ) (num (8)))
                                                ((convertNZ) (two))), 4)
        self.assertEqual((unchurch_int) ((divZ) ((convertNZ) (zero))
                                                ((convertNZ) (three))), 0)
        self.assertEqual((unchurch_int) ((divZ) ((neg) ((convertNZ) (num (99))))
                                                ((convertNZ) (num (4)))), -24)
        self.assertEqual((unchurch_int) ((divZ) ((neg) ((convertNZ) (num (275))))
                                                ((neg) ((convertNZ) (num (25))))), 11)



def main():
    unittest.main()

if __name__ == "__main__":
    main()
