__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

from lib import *
from fcc_aux import *
fcc1 = fcc(2,4)

fcc1.set_lattice_point(0,0,0,0,5)
fcc1.set_lattice_point(0,0,0,1,5)
fcc1.set_lattice_point(0,1,0,2,5)

make_fcc_xyz(fcc1)
