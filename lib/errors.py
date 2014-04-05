__author__ = 'Pranjal Goswami, QMEL IITKGP, http://pranjalgoswami.in'

class InputError(Exception):



         def __init__(self, value):
             self.value = value

         def __str__(self):
             return repr(self.value)

         def __repr__(self):
             return "Error : "+self.value
