__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

from lib import *
import numpy as np
import matplotlib.pyplot as plt
import aux

import matplotlib
from matplotlib import cm

n = 10
Nab_max = 3.0*n**2*(n-1)
print Nab_max
cube1 = Cube(n)
cube1.init_5050()

cube1.evaluate_interactions_with_surface_adjustment()
cube1.evaluate_interactions()

print cube1.interactions['Nab']
print cube1.sa_interactions['Nab']

print cube1.surface_interactions

N = 100
loop = True

x = list()
y = list()
z = list()
w = list()
v = list()

while(N <= 10000000 and loop):
    cube1.init_5050()
    cube1.evaluate_interactions()
    Nab = cube1.interactions['Nab']
    skipped_configurations=0
    y1=0
    for i in range(0,N):
        index = np.random.randint(0,n**3/2)
        target = np.random.randint(0,n**3/2)

        current_interactions_a = cube1.get_neighbours(cube1.a[index])
        current_interactions_b = cube1.get_neighbours(cube1.b[target])

        current_Nab = current_interactions_a['Nab']+\
                        current_interactions_b['Nab']
        next_Nab = current_interactions_a['Naa']+\
                    current_interactions_a['Nbb']+\
                    current_interactions_b['Naa']+\
                    current_interactions_b['Nbb']

        if(next_Nab>=current_Nab):
            cube1.swap(index,target)
            Nab = Nab - current_Nab + next_Nab
            cube1.evaluate_interactions_with_surface_adjustment()
            #print 'Nab:'+str(Nab)
            #print 'Nab_s :'+str(cube1.sa_interactions['Nab'])
            #print '_s_i :'+str(cube1.surface_interactions)
            '''
            print '% surface Interactions: '+\
                  str((cube1.surface_interactions\
                  *100.0)/cube1.sa_interactions['Nab'])+'% \n'

            print '%d\t%5.2f\t%5.2f\t%5.2f\t%5.2f\t'%(N,Nab,\
                cube1.sa_interactions['Nab'],\
                cube1.surface_interactions,\
                (cube1.surface_interactions\
                  *100.0)/cube1.sa_interactions['Nab'])
            y1+=1
            '''
            print('%d\t%d'%(i,N))

        else:
            skipped_configurations+=1

        x.append(i)
        y.append(Nab)
        z.append(cube1.sa_interactions['Nab'])
        w.append(cube1.surface_interactions)
        v.append((cube1.surface_interactions\
                  *100.0)/cube1.sa_interactions['Nab'])


    font = {'family' : 'serif',
            'color'  : 'blue',
            'weight' : 'normal',
            'size'   : 16,
            }
    fig = plt.figure()
    plt.title('%% Surface Interactions vs Iterations (N=%d)'%(N),fontdict=font)
    plt.xlabel("No. of Swaps")
    plt.ylabel("%% Surface Interactions")
    plt.ylim(0,100)
    plt.plot(x,v,'b-',label='Nab')
    #plt.plot(x,z,'g-.',label='Surface Adjusted Nab')
    #plt.plot(x,w,'r--.',label='Surface Interactions')
    #plt.legend()
    plt.savefig('output/N_si_percent_%d.png'%(N))

    N*=10
    loop = True
