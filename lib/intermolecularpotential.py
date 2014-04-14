import math
from lib.crystal import crystal
from lib.errors import InputError

__author__ = 'pranjal'

def calculateIntermolecularPotential(c,d):
    """
    Calculates and returns the InterMolecular Potential as sum of the
    Lennard Jones Potential and Electrostatic point charge potential

    Input: c is an object of type crystal and d is a dictionary that must
    contain, for each element occurring in crystal, the Lenard-Jones potential parameters
    and the point charges present on each element in the crystal

    The class crystal is defined in lib package
    The dictionary must be of the format give below :

        d = { ... , 8 : {'Name':'Oxygen', 'sigma' : 2.910, 'epsilon' : 6.11, 'q':0.01}, ...}

    The function then automatically evaluated the L-J potential parameters between unlike
    with Lorentz-Bertholet combination rules
    """
    if not isinstance(c,crystal):
        raise InputError("The passed parameter 'c' is not a valid crystal object")
    p = {} # dictionary for all ij parameters
    e = [] # list of all elements passed in the dictionary d
    vwp = 0 # Van der Waals Potential
    ecp = 0 # electrostatic point charge potential

    ke = 8.98755E9 # Coulombs constant
    Ke = 14.3 # Ke * ecp = electrostatic potential in eV
    #TODO : Validate format of dictionary d
    try:
        for Z,val in d.iteritems():
            e.append(Z)
        for i in range(0,len(e)):
            for j in range(0,len(e)):
                ij = str(e[i])+','+str(e[j])
                p[ij]  = {}
                p[ij]['sigma'] = (d[e[i]]['sigma']+d[e[j]]['sigma'])/2
                p[ij]['epsilon'] = math.sqrt(d[e[i]]['sigma']*d[e[j]]['sigma'])

    except:
        raise InputError("The passed parameter 'd' is not valid")

    N = len(c.lattice)

    for i in range(0,N-1):
        for j in range(i+1,N):
            ij = str(int(c.lattice[i].Z))+','+str(int(c.lattice[j].Z))
            r=c.getDistance(c.lattice[i],c.lattice[j])
            sigmaByR = p[ij]['sigma']/r
            vwp += p[ij]['epsilon']*(sigmaByR**12 - sigmaByR**6)
            ecp += d[c.lattice[i].Z]['q']*d[c.lattice[j].Z]['q']/r

    vwp = vwp*4*0.0104 # 0.0104 to convert it form kJ/mol to eV
    ecp = Ke*ecp

    #print vwp
    #print ecp
    return (vwp,ecp)