'''
Created on Dec 6, 2013

@author: thomas
'''

PROPERTIES = ['ductile', 'conductor', 'malleable', 'elasticity']

class Alkali():

    REACTION_LEVEL = 1

    CHARGE = -1

    def __init__(self, atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass


lithium = Alkali(3, 6.941)
sodium = Alkali(11, 22.98977)
potassium = Alkali(19, 29.0983)
rubidium = Alkali(37, 85.4678)
cesium = Alkali(55, 137.33)
francium = Alkali(87, 223)

class AlkalineEarthMetal():

    CHARGE = -2

    def __init__(self, atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass

beryllium = AlkalineEarthMetal(4, 9.01218)
magnesium = AlkalineEarthMetal(12, 24.305)
calcium = AlkalineEarthMetal(20, 40.08)
strontium = AlkalineEarthMetal(38, 87.62)
barium = AlkalineEarthMetal(56, 137.33)
radium = AlkalineEarthMetal(88, 226.025)