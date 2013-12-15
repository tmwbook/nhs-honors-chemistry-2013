'''
Created on Dec 15, 2013

@author: thomas
'''
from Metal import Metal

class AlkalineEarthMetal(Metal):

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