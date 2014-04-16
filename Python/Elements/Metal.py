'''
Created on Dec 6, 2013

@author: thomas
'''

PROPERTIES = ['ductile', 'conductor', 'malleable', 'elasticity', 'lustrous']

class Alkali():

    REACTION_LEVEL = 1

    CHARGE = 1

    def __init__(self, atomicNumber, atomicMass, lastElectConf):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass
        self.lastElectConf = lastElectConf


lithium = Alkali(3, 6.941, [" 2s^", "1"])
sodium = Alkali(11, 22.98977, [" 3s^", "1"])
potassium = Alkali(19, 29.0983, [" 4s^", "1"])
rubidium = Alkali(37, 85.4678, [" 5s^", "1"])
caesium = Alkali(55, 137.33, [" 6s^", "1"])
francium = Alkali(87, 223, [" 7s^", "1"])

class AlkalineEarthMetal():

    CHARGE = 2

    def __init__(self, atomicNumber, atomicMass, lastElectConf):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass
        self.lastElectConf = lastElectConf

beryllium = AlkalineEarthMetal(4, 9.01218, [" 2s^", "2"])
magnesium = AlkalineEarthMetal(12, 24.305, [" 3s^", "2"])
calcium = AlkalineEarthMetal(20, 40.08, [" 4s^", "2"])
strontium = AlkalineEarthMetal(38, 87.62, [" 5s^", "2"])
barium = AlkalineEarthMetal(56, 137.33, [" 6s^", "2"])
radium = AlkalineEarthMetal(88, 226.025, [" 7s^", "2"])