'''
Created on Dec 6, 2013

@author: thomas
'''
PROPERTIES = ['non malleable', 'non ductile', 'insulator', 'non elasticity']


class Halogen():

    CHARGE = 3

    def __init__(self, atomicNumber, atomicMass, lastElectConf):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass
        self.lastElectConf = lastElectConf

fluorine = Halogen(9, 18.998403, [" 1p^", "5"])
chlorine = Halogen(17, 35.453, [" 2p^", "5"])
bromine = Halogen(35, 79.904, [" 3p^", "5"])
iodine = Halogen(53, 126.905, [" 4p^", "5"])
astatine = Halogen(85, 210, [" 5p, 5"])


class Chalocogen():

    CHARGE = 3

    def __init__(self, atomicNumber, atomicMass, lastElectConf):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass
        self.lastElectConf = lastElectConf

oxygen = Chalocogen(8, 15.9994, [" 1p^", "4"])
sulfur = Chalocogen(16, 31.06, [" 2p^", "4"])
selenium = Chalocogen(34, 78.96, [" 3p^", "4"])
tellurium = Chalocogen(52, 127.6, [" 4p^", "4"])
polonium = Chalocogen(84, 209, [" 5p^", "4"])


class Pnictogen():

    CHARGE = 3

    def __init__(self, atomicNumber, atomicMass, lastElectConf):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass
        self.lastElectConf = lastElectConf

nitrogen = Pnictogen(7, 14.0067, [" 1p^", "3"])
phosphorus = Pnictogen(15, 30.97376, [" 2p^", "3"])
arsenic = Pnictogen(33, 74.9216, [" 3p^", "3"])
antimony = Pnictogen(51, 121.75, [" 4p^", "3"])
bismuth = Pnictogen(83, 209, [" 5p^", "3"])


class NobleGas():

    CHARGE = 0

    def __init__(self,atomicNumber, atomicMass, lastElectConf):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass
        self.lastElectronConf = lastElectConf

helium = NobleGas(2, 4.0026, [" 1p^", "6"])
neon = NobleGas(10, 20.179, [" 2p^", "6"])
argon = NobleGas(18, 39.948, [" 3p^", "6"])
krypton = NobleGas(36, 83.8, [" 4p^", "6"])
xenon = NobleGas(54, 131.29, [" 5p^", "6"])
radon = NobleGas(86, 222, [" 6p^", "6"])

class Extras():  # great class name btw, very descriptive /s
    def __init__(self, atomicNumber, atomicMass, lastElectConf):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass
        self.lastElectronConf = lastElectConf

boron = Extras(5, 10.81, [" 1p^", "1"])
aluminium = Extras(13, 26.981, [" 2p^", "1"])
gallium = Extras(31, 69.723, [" 3p^", "1"])
indium = Extras(49, 114.818, [" 4p^", "1"])
thallium = Extras(81, 204.38, [" 5p^", "1"])

carbon = Extras(6, 12.011, [" 1p^", "2"])
silicon = Extras(14, 28.085, [" 2p^", "2"])
germanium = Extras(32, 72.63, [" 3p^", "2"])
tin = Extras(50, 118.710, [" 4p^", "2"])
lead = Extras(82, 207.2, [" 5p^", "2"])

ununtrium = Extras(113, 284, [" 6p^", "1"])
flerovium = Extras(114, 289, [" 6p^", "2"])
ununpentium = Extras(115, 288, [" 6p^", "3"])
livemorium = Extras(116, 293, [" 6p^", "4"])
ununseptium = Extras(117, 294, [" 6p^", "5"])
ununoctium = Extras(118, 294, [" 6p^", "6"])#may move this to noble gas