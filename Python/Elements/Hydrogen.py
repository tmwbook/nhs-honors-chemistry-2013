'''
Created on March 29, 2014

@author: Thomas
'''

#Hydrogen is such a confusing element that we couldn't classify it, thus it has its own file. go you.


class Hydrogen(object):


    def __init__(self, atomicNumber, atomicMass, lastElectConf):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass
        self.lastElectConf = lastElectConf


hydrogen = Hydrogen(1, 1.00794, [" 1s^", "1"])