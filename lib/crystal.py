import math

__author__ = 'pranjal'

from latticePoint import *
from errors import *
class crystal:
    """ Model for a crystal lattice
        Contains an array of all the elements in the crystal lattice
        Each node in the list is [element, x, y, z]
    """

    def __init__(self):
        self.lattice = [] # lattice is an array of lattice points

    def addToLattice(self, l):
        if not isinstance(l,latticePoint):
            raise InputError("Parameter passed for crystal lattice is not a valid lattice point")

        self.lattice.append(l)

    def getDistance(self, l1, l2):
        """ Returns Cartesian Distance between two lattice points l1 and l2
        """
        if not isinstance(l1,latticePoint) or not isinstance(l2,latticePoint) :
            raise InputError("l1 and/or l2 is not a valid lattice point")
        r = math.sqrt((l1.x-l2.x)**2 + (l1.y-l2.y)**2 + (l1.z-l2.z)**2)
        return r