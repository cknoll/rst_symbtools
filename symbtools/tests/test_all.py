# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 11:35:00 2014

@author: Carsten Knoll
"""

import sys

if 'all' in sys.argv:
    FLAG_all = True
    sys.argv.remove('all')
else:
    FLAG_all = False

from test_core import *
from test_modeltools import *
from test_nctools import *

    
def main():
    unittest.main()

# see also the skip_slow logic at the beginning of the file
if __name__ == '__main__':
    main()
