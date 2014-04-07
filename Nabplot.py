__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'


from lib import *
import numpy as np
import matplotlib.pyplot as plt
import utils

n=2

data = dict()

N = 100000
for i in range(0,N):
    cube1 = Cube(n)
    cube1.init_random_5050()
    #aux.make_xyz(cube1)
    cube1.evaluate_interactions()
    print cube1.interactions['Nab']
    if cube1.interactions['Nab'] in data:
        data[cube1.interactions['Nab']]+=1
    else:
        data[cube1.interactions['Nab']]=1

print data

