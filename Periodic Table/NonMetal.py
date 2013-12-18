'''
Created on Dec 6, 2013

@author: thomas
'''
PROPERTIES = ['non malleable', 'non ductile', 'insulator', 'non elasticity']

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

class NobleGas(NonMetal):

    CHARGE = 0

    def __init__(self,atomicNumber, stomicMass):