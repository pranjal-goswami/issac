__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

from numpy import *
from site import *
from errors import *
import numbers

class Cube:


    def __init__(self, n=50):
        "Constructor for Cube"
        n = n+1 if n%2==1 else n
        self.n = n

        self.a = empty(n**3/2, dtype=object)
        self.b = empty(n**3/2, dtype=object)
        self.lattice=None

    def init_5050(self):
        s=0
        for i in range(0,self.n/2):
            for j in range(0,self.n):
                for k in range(0,self.n):
                    self.a[s]=Site(i,j,k)
                    self.b[self.n**3/2-s-1]=\
                        Site(self.n-i-1,self.n-j-1,self.n-k-1)
                    s+=1
        self.make_lattice()

    def init_homogeneous(self):
        sa=sb=s=0
        for i in range(0,self.n):
            for j in range(0,self.n):
                for k in range(0,self.n):
                    if((i+j+k)%2==0):
                        self.a[sa]=Site(i,j,k)
                        sa+=1
                    else:
                        self.b[sb]=Site(i,j,k)
                        sb+=1
                    s+=1
        self.make_lattice()

    def init_random_5050(self):
        self.lattice = zeros((self.n,self.n,self.n))
        c = 0
        c_max = self.n**3/2
        while(c<c_max):
            x = random.randint(0,self.n)
            y = random.randint(0,self.n)
            z = random.randint(0,self.n)
            if(self.lattice[x][y][z]==0):
                self.lattice[x][y][z]=1
                c+=1
        sa=sb=0
        for i in range(0,self.n):
            for j in range(0,self.n):
                for k in range(0,self.n):
                    if(self.lattice[i][j][k]==1):
                        self.b[sb]=Site(i,j,k)
                        sb+=1
                    else:
                        self.a[sa]=Site(i,j,k)
                        sa+=1






    def swap(self,index=None, target=None):
        #swap site at index in a and b
        if(index==None):
            raise InputError("Swap expects 1 arguments")
        if((index==int(index))!=True):
            raise InputError("Non integer parameter passed")
        if(index>=self.n**3/2):
            raise InputError("Index exceeds bounds")

        if(target==None):
            index_x=self.a[index].x
            index_y=self.a[index].y
            index_z=self.a[index].z
            target_x=self.b[index].x
            target_y=self.b[index].y
            target_z=self.b[index].z

            self.a[index],self.b[index] =self.b[index],self.a[index]

            self.lattice[index_x][index_y][index_z],\
                self.lattice[target_x][target_y][target_z]=\
                self.lattice[target_x][target_y][target_z],\
                self.lattice[index_x][index_y][index_z]

            return

        if((target==int(target))!=True):
            raise InputError("Non Integer parameter passed")
        if(target>=self.n**3/2):
            raise InputError("Index exceeds bounds")

        index_x=self.a[index].x
        index_y=self.a[index].y
        index_z=self.a[index].z
        target_x=self.b[target].x
        target_y=self.b[target].y
        target_z=self.b[target].z

        self.a[index],self.b[target]=self.b[target],self.a[index]

        self.lattice[index_x][index_y][index_z],\
            self.lattice[target_x][target_y][target_z]=\
            self.lattice[target_x][target_y][target_z],\
            self.lattice[index_x][index_y][index_z]

    def make_lattice(self):
        self.lattice = zeros((self.n,self.n,self.n))
        for i in range(0,self.n**3/2):
            self.lattice[self.b[i].x][self.b[i].y][self.b[i].z]=1


    def evaluate_interactions(self):
        #self.make_lattice()
        self.interactions = dict({'Naa':0,'Nab':0,'Nbb':0 })
        n = self.n

        for i in range(0,n):
            for j in range(0,n):
                for k in range(0,n):
                    atom = self.lattice[i][j][k]
                    #in lattice b is 1 and a is 0
                    #
                    if(i!=n-1):
                        neighbour = self.lattice[i+1][j][k]
                        if((atom+neighbour)==0):
                            self.interactions['Naa']+=1
                        elif((atom+neighbour==1)):
                            self.interactions['Nab']+=1
                        elif((atom+neighbour)==2):
                            self.interactions['Nbb']+=1

                    if(j!=n-1):
                        neighbour = self.lattice[i][j+1][k]
                        if((atom+neighbour)==0):
                            self.interactions['Naa']+=1
                        elif((atom+neighbour==1)):
                            self.interactions['Nab']+=1
                        elif((atom+neighbour)==2):
                            self.interactions['Nbb']+=1

                    if(k!=n-1):
                        neighbour = self.lattice[i][j][k+1]
                        if((atom+neighbour)==0):
                            self.interactions['Naa']+=1
                        elif((atom+neighbour==1)):
                            self.interactions['Nab']+=1
                        elif((atom+neighbour)==2):
                            self.interactions['Nbb']+=1

    def evaluate_interactions_with_surface_adjustment(self):
        #self.make_lattice()
        #surface adjusted interactions
        self.sa_interactions = dict({'Naa':0,'Nab':0,'Nbb':0 })
        n = self.n
        depth_offset = 0.05
        d = depth_offset*n
        c = 1.6 #coefficient for surface adjustment
        s_interactions = 0 #surface interactions
        for i in range(0,n):
            for j in range(0,n):
                for k in range(0,n):
                    atom = self.lattice[i][j][k]
                    #in lattice b is 1 and a is 0
                    #
                    if(i!=n-1):
                        neighbour = self.lattice[i+1][j][k]
                        if((atom+neighbour)==0):
                            self.sa_interactions['Naa']+=1
                        elif((atom+neighbour==1)):
                            if(self.is_in_surface(i,j,k,d,n)):
                                s_interactions+=1
                                self.sa_interactions['Nab']+=1*c
                            else:
                                self.sa_interactions['Nab']+=1
                        elif((atom+neighbour)==2):
                            self.sa_interactions['Nbb']+=1

                    if(j!=n-1):
                        neighbour = self.lattice[i][j+1][k]
                        if((atom+neighbour)==0):
                            self.sa_interactions['Naa']+=1
                        elif((atom+neighbour==1)):
                            if(self.is_in_surface(i,j,k,d,n)):
                                s_interactions+=1
                                self.sa_interactions['Nab']+=1*c
                            else:
                                self.sa_interactions['Nab']+=1
                        elif((atom+neighbour)==2):
                            self.sa_interactions['Nbb']+=1

                    if(k!=n-1):
                        neighbour = self.lattice[i][j][k+1]
                        if((atom+neighbour)==0):
                            self.sa_interactions['Naa']+=1
                        elif((atom+neighbour==1)):
                            if(self.is_in_surface(i,j,k,d,n)):
                                s_interactions+=1
                                self.sa_interactions['Nab']+=1*c
                            else:
                                self.sa_interactions['Nab']+=1
                        elif((atom+neighbour)==2):
                            self.sa_interactions['Nbb']+=1
        self.surface_interactions = s_interactions


    def get_neighbours(self, site):
        site.neighbours = {'Naa':0, 'Nab':0, 'Nbb':0}
        x=site.x
        y=site.y
        z=site.z
        n=self.n
        atom = self.lattice[x][y][z]
        if(x!=n-1):
            neighbour = self.lattice[x+1][y][z]
            if((atom+neighbour)==0): site.neighbours['Naa']+=1
            elif((atom+neighbour==1)): site.neighbours['Nab']+=1
            elif((atom+neighbour)==2): site.neighbours['Nbb']+=1
        if(x!=0):
            neighbour = self.lattice[x-1][y][z]
            if((atom+neighbour)==0): site.neighbours['Naa']+=1
            elif((atom+neighbour==1)): site.neighbours['Nab']+=1
            elif((atom+neighbour)==2): site.neighbours['Nbb']+=1
        if(y!=n-1):
            neighbour = self.lattice[x][y+1][z]
            if((atom+neighbour)==0): site.neighbours['Naa']+=1
            elif((atom+neighbour==1)): site.neighbours['Nab']+=1
            elif((atom+neighbour)==2): site.neighbours['Nbb']+=1
        if(y!=0):
            neighbour = self.lattice[x][y-1][z]
            if((atom+neighbour)==0): site.neighbours['Naa']+=1
            elif((atom+neighbour==1)): site.neighbours['Nab']+=1
            elif((atom+neighbour)==2): site.neighbours['Nbb']+=1
        if(z!=n-1):
            neighbour = self.lattice[x][y][z+1]
            if((atom+neighbour)==0): site.neighbours['Naa']+=1
            elif((atom+neighbour==1)): site.neighbours['Nab']+=1
            elif((atom+neighbour)==2): site.neighbours['Nbb']+=1
        if(z!=0):
            neighbour = self.lattice[x][y][z-1]
            if((atom+neighbour)==0): site.neighbours['Naa']+=1
            elif((atom+neighbour==1)): site.neighbours['Nab']+=1
            elif((atom+neighbour)==2): site.neighbours['Nbb']+=1

        return site.neighbours

    @staticmethod
    def is_in_surface(i,j,k,d,n):
        if(i<=d or j<=d or k<=d ):
            return True
        if(i>(n-d-1) or j>(n-d-1) or k>(n-d-1)):
            return True
        return False
























