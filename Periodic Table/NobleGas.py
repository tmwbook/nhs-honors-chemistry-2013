'''
Created on Dec 6, 2013

@author: thomas
'''

from NonMetal import NonMetal

class NobleGas(NonMetal):
    
    REACTION_LEVEL = 0

    CHARGE = 0

    def __init__(self, atomicNumber, atomicMass):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass

neon = NobleGas(10, 20.179)
argon = NobleGas(18, 39.948)
krypton = NobleGas(36, 83.8)
xenon = NobleGas(54, 131.29)
radon = NobleGas(86, 222)