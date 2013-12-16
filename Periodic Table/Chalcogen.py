'''
Created on Dec 15, 2013

@author: thomas
'''
from NonMetal import NonMetal

class Chalocogen(NonMetal):

    CHARGE = 3

    def __init__(self, atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass

oxygen = Chalocogen(8, 15.9994)
sulfur = Chalocogen(16, 31.06)
selenium = Chalocogen(34, 78.96)
tellurium = Chalocogen(52, 127.6)
polonium = Chalocogen(84, 209)