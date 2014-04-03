'''
Created on Dec 6, 2013

@author: thomas
'''
PROPERTIES = ['non malleable', 'non ductile', 'insulator', 'non elasticity']


class Halogen():

    CHARGE = 3

    def __init__(self, atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass

fluorine = Halogen(9, 18.998403)
chlorine = Halogen(17, 35.453)
bromine = Halogen(35, 79.904)
iodine = Halogen(53, 126.905)
astatine = Halogen(85, 210)


class Chalocogen():

    CHARGE = 3

    def __init__(self, atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass

oxygen = Chalocogen(8, 15.9994)
sulfur = Chalocogen(16, 31.06)
selenium = Chalocogen(34, 78.96)
tellurium = Chalocogen(52, 127.6)
polonium = Chalocogen(84, 209)


class Pnictogen():

    CHARGE = 3

    def __init__(self, atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass

nitrogen = Pnictogen(7, 14.0067)
phosphorus = Pnictogen(15, 30.97376)
arsenic = Pnictogen(33, 74.9216)
antimony = Pnictogen(51, 121.75)
bismuth = Pnictogen(83, 209)


class NobleGas():

    CHARGE = 0

    def __init__(self,atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass

helium = NobleGas(2, 4.0026)
neon = NobleGas(10, 20.179)
argon = NobleGas(18, 39.948)
krypton = NobleGas(36, 83.8)
xenon = NobleGas(54, 131.29)
radon = NobleGas(86, 222)

class Extras():
    def __init__(self, atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass

boron = Extras(5, 10.81)
aluminium = Extras(13, 26.981)
gallium = Extras(31, 69.723)
indium = Extras(49, 114.818)
thallium = Extras(81, 204.38)

carbon = Extras(6, 12.011)
silicon = Extras(14, 28.085)
germanium = Extras(32, 72.63)
tin = Extras(50, 118.710)
lead = Extras(82, 207.2)

ununtrium = Extras(113, 284)
flerovium = Extras(114, 289)
ununpentium = Extras(115, 288)
livemorium = Extras(116, 293)
ununseptium = Extras(117, 294)
ununoctium = Extras(118, 294)#may move this to nobel gas