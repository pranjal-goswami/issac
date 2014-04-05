__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

from numpy import *
from site import *
from errors import *
import numbers


class fcc:


    def __init__(self, n=50,a=1):
        "Constructor for FCC Structure"

        '''
        A FCC structure is broken down into 4 three dimensional matrices
        cube - n x n x n
        fc_x - n x (n-1) x (n-1)
        fc_y - (n-1) x n x (n-1)
        fc_z - (n-1) x (n-1) x n
        '''
        if n % 2 !=0 :
            n=n+1
        self.n = n
        self.a = a

        self.cube = zeros((self.n,self.n,self.n))
        self.fcx = zeros((self.n,self.n-1,self.n-1))
        self.fcy = zeros((self.n-1,self.n,self.n-1))
        self.fcz = zeros((self.n-1,self.n-1,self.n))


    # lattice point setter
    def set_lattice_point(self,x,y,z,norm,value):
        "Set value of lattice point"
        n = self.n

        if(x >= n or y >= n or z >= n):
            raise InputError('Index out of bounds')
        if(norm == 0):
            self.cube[x][y][z] = value

        elif(norm == 1):
            if(y>=n-1 or z >= n-1):
                raise InputError('Invalid Index for X-normal Face')
            self.fcx[x][y][z] = value

        elif(norm == 2):
            if(x>=n-1 or z >= n-1):
                raise InputError('Invalid Index for Y-normal Face')
            self.fcy[x][y][z] = value

        elif(norm == 3):
            if(x>=n-1 or y >= n-1):
                raise InputError('Invalid Index for Z-normal Face')
            self.fcz[x][y][z] = value



    # lattice point getter
    def get_lattice_point(self,x,y,z,norm):
        n = self.n

        if(x >= n or y >= n or z >= n):
            raise InputError('Index out of bounds')
        if(norm == 0):
            value = self.cube[x][y][z]

        elif(norm == 1):
            if(y>=n-1 or z >= n-1):
                raise InputError('Invalid Index for X-normal Face')
            value = self.fcx[x][y][z]

        elif(norm == 2):
            if(x>=n-1 or z >= n-1):
                raise InputError('Invalid Index for Y-normal Face')
            value = self.fcy[x][y][z]

        elif(norm == 3):
            if(x>=n-1 or y >= n-1):
                raise InputError('Invalid Index for Z-normal Face')
            value = self.fcz[x][y][z]

        return value




    def init_homogeneous(self,x):
        "Initialize the FCC nano particle for homogeneous configuration with A:B as x:1"
        # Current assumption -> x:1 is always greater than 1
        # A --> Cerium [0] || B --> Tin [1]
        n = self.n
        for i in range(0,n):
            for j in range(0,n):
                r = (i+j)%(x+1)
                for k in range(0,n):
                    if((k+1)%(x+1)==r):
                        self.set_lattice_point(i,j,k,0,1)























