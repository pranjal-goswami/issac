__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

from numpy.core.fromnumeric import size
from fcc_aux import *
from lib.intermolecularpotential import *
from lib.fcc import fcc
from utils import *
import numpy as np

fcc1 = fcc(2,5.41122,50)
#fcc1.init_homogeneous(1,58)

d = {
    58:{'Name':'Cerium','Symbol':'Ce','sigma':3.2,'epsilon':69.08,'q':2},
    50:{'Name':'Tin','Symbol':'Sn','sigma':2.51,'epsilon':0.5,'q':2},
    78:{'Name':'Platinum','Symbol':'Pt','sigma':2.65,'epsilon':0.6,'q':2},
    8:{'Name':'Oxygen','Symbol':'O','sigma':2.6,'epsilon':3.78,'q':-1}
}

c = fcc1.makeCrystalLattice()
k = len(c.lattice)
x = 0.2

for i in range(0,10000):
    fcc1 = fcc(20,5.41122,50)
    c = fcc1.makeCrystalLattice()
    k = len(c.lattice)
    rand = np.random.randint(0,k,size=(int(k*x),))
    for r in rand:
        c.lattice[r].Z=78
    c = fcc1.addOxygen(c)

    #makeXYZFromCrystal(c,d)
    E = calculateIntermolecularPotential(c,d)
    print E
