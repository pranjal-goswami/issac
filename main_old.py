__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

from lib import *
import numpy as np
import matplotlib.pyplot as plt
import aux

import matplotlib
from matplotlib import cm

n = 10
Nab_max = 3.0*n**2*(n-1)
#print Nab_max
cube1 = Cube(n)
cube1.init_5050()

skipped_configurations = 0
N = 100
loop = True

x = list()
y = list()
z = list()

while(N <= 10000 and loop):
    cube1.init_5050()
    skipped_configurations=0
    y1=0
    #print 'skipped = '+str(skipped_configurations)
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
            y1+=1
        else:
            skipped_configurations+=1


        if(i%100==0):

            y.append(y1)
            y1=0
            x.append(i/100)
    N*=10
    loop = False

aux.make_xyz(cube1)

print x
print y

font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }

X,Z = np.meshgrid(x,z)

plt.plot(x,y)
plt.show()

#y = ((Z**2 - 1)**2)
'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.title('% A vs layer', fontdict=font)
ax.set_xlabel('layer', fontdict=font)
ax.set_zlabel('% A', fontdict=font)
ax.set_ylabel('No. of Swaps', fontdict=font)

ax.plot_wireframe(X, Z, y, rstride=1, cstride=1, linewidth=1, cmap=cm.YlGnBu_r)
#p.set_alpha(0.7)
plt.show()
'''