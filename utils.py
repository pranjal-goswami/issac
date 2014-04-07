__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

from lib import *


def make_xyz(cube):
    n =cube.n
    print n**3
    print "title"
    for i in range(0,n**3/2):
        print "Pt   "+str(cube.a[i].x*1.5)+"   "\
              +str(cube.a[i].y*1.5)+"   "+str(cube.a[i].z*1.5)
    for i in range(0,n**3/2):
        print "Au   "+str(cube.b[i].x*1.5)+"   "\
              +str(cube.b[i].y*1.5)+"   "+str(cube.b[i].z*1.5)


def layer_composition(cube):
    n = cube.n
    # assuming n is even // a
    layers = dict()
    l_max = n/2

    for l in range(1,l_max+1):
        o=l-1
        e=n-o
        layers[l]={'a':0, 'b':0}

        #for back face
        for i in range(o,e):
            for j in range(o,e):
                if(cube.lattice[i][j][o]==0):
                    layers[l]['a']+=1
                else:
                    layers[l]['b']+=1
        #for front face
        for i in range(o,e):
            for j in range(o,e):
                if(cube.lattice[i][j][e-1]==0):
                    layers[l]['a']+=1
                else:
                    layers[l]['b']+=1
        #for left face
        for j in range(o,e):
            for k in range(o+1,e-1):
                if(cube.lattice[o][j][k]==0):
                    layers[l]['a']+=1
                else:
                    layers[l]['b']+=1
        #for right face
        for j in range(o,e):
            for k in range(o+1,e-1):
                if(cube.lattice[e-1][j][k]==0):
                    layers[l]['a']+=1
                else:
                    layers[l]['b']+=1
        #for top face
        for i in range(o+1,e-1):
            for k in range(o+1,e-1):
                if(cube.lattice[i][o][k]==0):
                    layers[l]['a']+=1
                else:
                    layers[l]['b']+=1
        #for bottom face
        for i in range(o+1,e-1):
            for k in range(o+1,e-1):
                if(cube.lattice[i][e-1][k]==0):
                    layers[l]['a']+=1
                else:
                    layers[l]['b']+=1

    return layers
