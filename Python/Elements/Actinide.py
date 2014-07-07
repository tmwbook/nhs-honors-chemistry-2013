'''
Created on April 2, 2014

@author: Thomas
'''


class Actinide(object):


    def __init__(self, atomicNumber, atomicMass, lastElectConf):
        self.atomicNumber = atomicNumber
        self.atomicMass = atomicMass
        self.lastElectConf = lastElectConf

actinium = Actinide(89, 227, [" 6d^", "1"])
thorium = Actinide(90, 232.03, [" 5f^", "1"])
protactinium = Actinide(91, 231.03, [" 5f^", "2"])
uranium = Actinide(92, 238.02, [" 5f^", "3"])
neptunium = Actinide(93, 273, [" 5f^", "4"])
plutonium = Actinide(94, 244, [" 5f^", "5"])

americium = Actinide(95, 243, [" 5f^", "6"])
curium = Actinide(96, 247, [" 5f^", "7"])
berkelium = Actinide(97, 247, [" 5f^", "8"])
californium = Actinide(98, 251, [" 5f^", "9"])
einsteinium = Actinide(99, 252, [" 5f^", "10"])
fermium = Actinide(100, 257, [" 5f^", "11"])

mendelevium = Actinide(101, 258, [" 5f^", "12"])
nobelium = Actinide(102, 259, [" 5f^", "13"])
lawrencium = Actinide(103, 262, [" 5f^", "14"])