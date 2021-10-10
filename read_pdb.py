#! /usr/bin/python
import sys
from getopt import getopt
import numpy as np
from biopandas.pdb import PandasPdb

ppdb = PandasPdb()

S = ppdb.read_pdb('./sample.pdb')
print(S)


