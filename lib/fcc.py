__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

from numpy import *
from site import *
from errors import *
from crystal import *
from latticePoint import *


class fcc:
    """
    A FCC structure is broken down into 4 three dimensional matrices
    cube - n x n x n
    fc_x - n x (n-1) x (n-1)
    fc_y - (n-1) x n x (n-1)
    fc_z - (n-1) x (n-1) x n
    """

    def __init__(self, n=50, a=1, Z=58):
        if n % 2 != 0:
            n = n + 1
        self.n = n
        self.a = a
        self.Z = Z

        self.cube = zeros((self.n, self.n, self.n))
        self.fcx = zeros((self.n, self.n - 1, self.n - 1))
        self.fcy = zeros((self.n - 1, self.n, self.n - 1))
        self.fcz = zeros((self.n - 1, self.n - 1, self.n))

        #instantiation with passed atomic number
        for i in range(0,n):
            for j in range(0,n):
                for k in range(0,n):
                    self.set_lattice_point(i, j, k, 0, Z)
        for i in range(0,n):
            for j in range(0,n-1):
                for k in range(0,n-1):
                    self.set_lattice_point(i, j, k, 1, Z)
        for i in range(0,n-1):
            for j in range(0,n):
                for k in range(0,n-1):
                    self.set_lattice_point(i, j, k, 2, Z)
        for i in range(0,n-1):
            for j in range(0,n-1):
                for k in range(0,n):
                    self.set_lattice_point(i, j, k, 3, Z)


    def set_lattice_point(self, x, y, z, norm, value):
        """Set value of lattice point"""
        n = self.n

        if (x >= n or y >= n or z >= n):
            raise InputError('Index out of bounds')
        if (norm == 0):
            self.cube[x][y][z] = value

        elif (norm == 1):
            if (y >= n - 1 or z >= n - 1):
                raise InputError('Invalid Index for X-normal Face')
            self.fcx[x][y][z] = value

        elif (norm == 2):
            if (x >= n - 1 or z >= n - 1):
                raise InputError('Invalid Index for Y-normal Face')
            self.fcy[x][y][z] = value

        elif (norm == 3):
            if (x >= n - 1 or y >= n - 1):
                raise InputError('Invalid Index for Z-normal Face')
            self.fcz[x][y][z] = value


    def get_lattice_point(self, x, y, z, norm):
        """lattice point getter """
        n = self.n
        value = -1

        if (x >= n or y >= n or z >= n):
            raise InputError('Index out of bounds')
        if (norm == 0):
            value = self.cube[x][y][z]

        elif (norm == 1):
            if (y >= n - 1 or z >= n - 1):
                raise InputError('Invalid Index for X-normal Face')
            value = self.fcx[x][y][z]

        elif (norm == 2):
            if (x >= n - 1 or z >= n - 1):
                raise InputError('Invalid Index for Y-normal Face')
            value = self.fcy[x][y][z]

        elif (norm == 3):
            if (x >= n - 1 or y >= n - 1):
                raise InputError('Invalid Index for Z-normal Face')
            value = self.fcz[x][y][z]

        return value


    def init_homogeneous(self, x, Za, Zb=None):
        """Initialize the FCC nano particle for homogeneous configuration with A:B as x:1
        Current assumption -> x:1 is always greater than 1
        A --> Cerium [58] || B --> Tin [50]
        """
        n = self.n
        if Zb == None : Zb = self.Z
        for i in range(0, n):
            for j in range(0, n):
                r = (i + j) % (x + 1)
                for k in range(0, n):
                    if (k + 1) % (x + 1) == r:
                        self.set_lattice_point(i, j, k, 0, Za)
                    else:
                        self.set_lattice_point(i, j, k, 0, Zb)

        for i in range(0, n):
            for j in range(0, n-1):
                r = (i + j) % (x + 1)
                for k in range(0, n-1):
                    if (k + 1) % (x + 1) == r:
                        self.set_lattice_point(i, j, k, 1, Za)
                    else:
                        self.set_lattice_point(i, j, k, 1, Zb)

        for i in range(0, n-1):
            for j in range(0, n):
                r = (i + j) % (x + 1)
                for k in range(0, n-1):
                    if (k + 1) % (x + 1) == r:
                        self.set_lattice_point(i, j, k, 2, Za)
                    else:
                        self.set_lattice_point(i, j, k, 2, Zb)

        for i in range(0, n-1):
            for j in range(0, n-1):
                r = (i + j) % (x + 1)
                for k in range(0, n):
                    if (k + 1) % (x + 1) == r:
                        self.set_lattice_point(i, j, k, 3, Za)
                    else:
                        self.set_lattice_point(i, j, k, 3, Zb)




    def makeCrystalLattice(self):
        """ Create a crystal lattice in c from the fcc structure
        """
        c = crystal()
        a = self.a
        n = self.n
        # first the cube
        for i in range(0, n):
            for j in range(0, n):
                for k in range(0, n):
                    c.addToLattice(latticePoint(self.cube[i][j][k], i * a, j * a, k * a))

        # the X normal face atoms
        for i in range(0, n):
            for j in range(0, n - 1):
                for k in range(0, n - 1):
                    c.addToLattice(latticePoint(self.fcx[i][j][k], i * a, j * a + a / 2, k * a + a / 2))

        # the Y normal face atoms
        for i in range(0, n - 1):
            for j in range(0, n):
                for k in range(0, n - 1):
                    c.addToLattice(latticePoint(self.fcy[i][j][k], i * a + a / 2, j * a, k * a + a / 2))

        # the Z normal face atoms
        for i in range(0, n - 1):
            for j in range(0, n - 1):
                for k in range(0, n):
                    c.addToLattice(latticePoint(self.fcz[i][j][k], i * a + a / 2, j * a + a / 2, k * a))

        return c

    def addOxygen(self,c):
        a =self.a
        aBy4 = a/4
        n = self.n
        for i in range(0,2*(n-1)):
            for j in range(0,2*(n-1)):
                for k in range(0,2*(n-1)):
                    c.addToLattice(latticePoint(8, aBy4 + i * a / 2,aBy4 + j * a / 2, aBy4+ k* a/2))
        return c






















