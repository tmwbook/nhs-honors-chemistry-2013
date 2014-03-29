'''
Created on Jan 14, 2014

@author: Thomas
'''
from Metal import PROPERTIES


class TransitionMetal():

    PROPERTIES = PROPERTIES

    def __init__(self, atomicNumber, atomicMass, charge):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass
        self.charge = charge