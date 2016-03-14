# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 11:35:00 2014

@author: Carsten Knoll
"""

import unittest
import sys

import sympy as sp
from sympy import sin, cos, exp

import numpy as np
import scipy as sc
import scipy.integrate

import symbtools as st
import inspect
from IPython import embed as IPS


if 'all' in sys.argv:
    FLAG_all = True
    sys.argv.remove('all')
else:
    FLAG_all = False


# own decorator for skipping slow tests
def skip_slow(func):
    return unittest.skipUnless(FLAG_all, 'skipping slow test')(func)

# Avoid warnings of undefined symbols from the IDE,
# but still make use of st.make_global
x1 = x2 = x3 = x4 = None
y1 = y2 = None
a1 = z4 = z7 = z10 = None


class InteractiveConvenienceTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_no_IPS_call(self):
        """
        test whether there is some call to interactive IPython (leagacy from debugging)
        """
        srclines = inspect.getsourcelines(st)[0]

        def filter_func(tup):
            idx, line = tup
            return 'IPS()' in line and not line.strip()[0] == '#'

        res = filter(filter_func, enumerate(srclines, 1))

        self.assertEqual(res, [])

    
def main():
    unittest.main()

# see also the skip_slow logic at the beginning of the file
if __name__ == '__main__':
    main()
