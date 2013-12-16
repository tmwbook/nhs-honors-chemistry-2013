'''
Created on Dec 15, 2013

@author: thomas
'''
from NonMetal import NonMetal

class Halogen(NonMetal):

    CHARGE = 3

    def __init__(self, atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass

fluorine = Halogen(9, 18.998403)
chlorine = Halogen(17, 35.453)
bromine = Halogen(35, 79.904)
iodine = Halogen(53, 126.905)
astatine = Halogen(85, 210)