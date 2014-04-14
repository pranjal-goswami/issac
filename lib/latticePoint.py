__author__ = 'pranjal'

class latticePoint:
    """Model for a lattice point. Each lattice point contains element(the atomic number) and x y z coordinates"""

    def __init__(self, Z=1, x=0, y=0, z=0):
        """ Constructor for latticePoint
        """
        self.Z = Z #default element is Hydrogen (Z = 1)
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "<[%s](%s,%s,%s)>" %(self.Z,self.x,self.y,self.z)

    def __str__(self):
        return "[%s](%s,%s,%s)" % (self.Z,self.x, self.y, self.z)
