'''
Created on Dec 15, 2013

@author: thomas
'''
from NonMetal import NonMetal

class Pnictogen(NonMetal):

    CHARGE = 3

    def __init__(self, atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass

nitrogen = Pnictogen(7, 14.0067)
phosphorus = Pnictogen(15, 30.97376)
arsenic = Pnictogen(33, 74.9216)
antimony = Pnictogen(51, 121.75)
bismuth = Pnictogen(83, 209)