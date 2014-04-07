__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

from lib import *
import numpy as np
import matplotlib.pyplot as plt
import utils
import matplotlib

n=10
cube1 = Cube(n)
nab = dict()
x = list()
y = list()

N=100000

x.append(n**2)
y.append(1*100.0/N)



for i in range(0,N):
    if(i%100==0): print str(i*100.0/N)+'%'
    cube1.init_random_5050()
    cube1.evaluate_interactions()
    #print cube1.interactions['Nab']
    if cube1.interactions['Nab'] in nab:
        nab[cube1.interactions['Nab']]+=1
    else:
        nab[cube1.interactions['Nab']]=1

print nab
for key in nab.iterkeys():
    x.append(key)
    y.append(nab[key]*100.0/N)

x.append(3*n**2*(n-1))
y.append(1*100.0/N)

print x
print y
plt.plot(x,y,'ro')
plt.savefig('./output/graphs/nab_'+str(n)+'_'+str(N)+'.png')
plt.show()
