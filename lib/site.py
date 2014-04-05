__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

class Site:


    def __init__(self,x=0,y=0,z=0):
        "Coordinates of a particular site"
        self.x=x
        self.y=y
        self.z=z

    def __repr__(self):
        return "<(%s,%s,%s)>" %(self.x,self.y,self.z)

    def __str__(self):
        return "(%s,%s,%s)" % (self.x, self.y, self.z)