'''
Created on April 2, 2014

@author: Thomas
'''


class Lanthanide(object):

    def __init__(self, atomicNumber, atomicMass, lastElectConf):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass
        self.lastElectConf = lastElectConf


lanthanum = Lanthanide(57, 138.9, [" 5d^", "1"])
cerium = Lanthanide(58, 140.116, [" 4f^", "1"])
praseodymium = Lanthanide(59, 140.9, [" 4f^", "2"])
neodymium = Lanthanide(60, 144.242, [" 4f^", "3"])
promethium = Lanthanide(61, 145, [" 4f^", "4"])
samarium = Lanthanide(62, 150.36, [" 4f^", "5"])

europium = Lanthanide(63, 151.964, [" 4f^", "6"])
gadolinium = Lanthanide(64, 157.25, [" 4f^", "7"])
terbium = Lanthanide(65, 158.92, [" 4f^", "8"])
dysprosium = Lanthanide(66, 162.5, [" 4f^", "9"])
holmium = Lanthanide(67, 164.93, [" 4f^", "10"])
erbium = Lanthanide(68, 167.259, [" 4f^", "11"])

thulium = Lanthanide(69, 168.93, [" 4f^", "12"])
ytterbium = Lanthanide(70, 173.054, [" 4f^", "13"])
lutetium = Lanthanide(71, 174.6338, ["4f^", "14"])