'''
Created on Dec 6, 2013

@author: thomas
'''

import Metal
import NonMetal

NUMBER_OF_ELEMENTS = 118

class Table(object):
    NUMBER_OF_ELEMENTS = 118 #something to stop an error
    #Now that I think of it I may not need this class at all, we will see

elementLocations = {'lithium': Metal.lithium, 'sodium': Metal.sodium, 'potassium': Metal.potassium, 'rubidium': Metal.rubidium,
                    'cesium': Metal.cesium, 'francium': Metal.francium, 'beryllium': Metal.beryllium, 'magnesium': Metal.magnesium,
                    'calcium': Metal.calcium, 'strontium': Metal.strontium, 'barium': Metal.barium, 'radium': Metal.radium,
                    'fluorine': NonMetal.fluorine, 'chlorine': NonMetal.chlorine, 'bromine': NonMetal.bromine,
                    'iodine': NonMetal.iodine, 'astatine': NonMetal.astatine, 'oxygen': NonMetal.oxygen, 'sulfur': NonMetal.sulfur,
                    'selenium': NonMetal.selenium, 'tellurium': NonMetal.tellurium, 'polonium': NonMetal.polonium,
                    'nitrogen': NonMetal.nitrogen, 'phosphorus': NonMetal.phosphorus, 'arsenic': NonMetal.arsenic,
                    'antimony': NonMetal.antimony, 'bismuth': NonMetal.bismuth, 'helium': NonMetal.helium, 'neon': NonMetal.neon,
                    'argon': NonMetal.argon, 'krypton': NonMetal.krypton, 'xenon': NonMetal.xenon, 'radon': NonMetal.radon}
                    #Add locations of Elements in the inner and outer transition metals