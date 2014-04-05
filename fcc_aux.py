__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

from lib import *

def make_fcc_xyz(fcc1):
    n =fcc1.n
    print n**3 + 3*((n-1)**2)*n
    print "title"
    offset = fcc1.a / 2
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                atom = "Pt " if fcc1.cube[i][j][k]==5 else "Si "
                print atom+str(i*fcc1.a)+" "+str(j*fcc1.a)+" "+str(k*fcc1.a)

    for i in range(0,n):
        for j in range(0,n-1):
            for k in range(0,n-1):
                atom = "Pt " if fcc1.fcx[i][j][k]==5 else "Si "
                print atom+str(i*fcc1.a)+" "+str(j*fcc1.a + offset)+" "+str(k*fcc1.a + offset)

    for i in range(0,n-1):
        for j in range(0,n):
            for k in range(0,n-1):
                atom = "Pt " if fcc1.fcy[i][j][k]==5 else "Si "
                print atom+str(i*fcc1.a + offset)+" "+str(j*fcc1.a)+" "+str(k*fcc1.a + offset)

    for i in range(0,n-1):
        for j in range(0,n-1):
            for k in range(0,n):
                atom = "Pt " if fcc1.fcz[i][j][k]==5 else "Si "
                print atom+str(i*fcc1.a + offset)+" "+str(j*fcc1.a + offset)+" "+str(k*fcc1.a)

