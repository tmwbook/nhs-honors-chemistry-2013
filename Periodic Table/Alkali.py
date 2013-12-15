'''
Created on Dec 6, 2013

@author: thomas
'''

import Metal

class Alkali(Metal):
    
    REACTION_LEVEL = 1
    
    def __init__(self, atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass


lithum = Alkali(3, 6.941)
sodium = Alkali(11, 22.98977)
potassium = Alkali(19, 29.0983)
rubidium = Alkali(37, 85.4678)
cesium = Alkali(55, 137.33)
francium = Alkali(87, 223)