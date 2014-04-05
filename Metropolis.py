import random
import math
def metropolis(current,new):
    # First Guess Should Be A Good One
    # Current is the initial energy & New is the energy of the new like wise
    Boltzman=1.3806488*10e-23
    Temperature=300
    random_number= random.random()
    # Generate a Random Number
    print random_number
    probability_ratio=math.exp((current-new)/(Boltzman*Temperature))
    if probability_ratio > random_number:
        return new
    else:
        return current
metropolis(20,30)


