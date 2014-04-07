__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

from lib import *
import numpy as np
import matplotlib.pyplot as plt
import utils
import matplotlib

n=15
cube1 = Cube(n)
cube1.init_5050()

N=100000

for i in range(0,N):
        index = np.random.randint(0,n**3/2)
        target = np.random.randint(0,n**3/2)
        cube1.swap(index,target)

utils.make_xyz(cube1)