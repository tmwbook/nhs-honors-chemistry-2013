'''
Created on Dec 6, 2013

@author: thomas
'''

import Elements.Metal
import Elements.NonMetal

NUMBER_OF_ELEMENTS = 118


elementLocations = {'lithium': Elements.Metal.lithium, 'sodium': Elements.Metal.sodium,
                    'potassium': Elements.Metal.potassium, 'rubidium': Elements.Metal.rubidium,
                    'cesium': Elements.Metal.cesium, 'francium': Elements.Metal.francium,
                    'beryllium': Elements.Metal.beryllium, 'magnesium': Elements.Metal.magnesium,
                    'calcium': Elements.Metal.calcium, 'strontium': Elements.Metal.strontium,
                    'barium': Elements.Metal.barium, 'radium': Elements.Metal.radium,
                    'fluorine': Elements.NonMetal.fluorine, 'chlorine': Elements.NonMetal.chlorine,
                    'bromine': Elements.NonMetal.bromine, 'iodine': Elements.NonMetal.iodine,
                    'astatine': Elements.NonMetal.astatine, 'oxygen': Elements.NonMetal.oxygen,
                    'sulfur': Elements.NonMetal.sulfur, 'selenium': Elements.NonMetal.selenium,
                    'tellurium': Elements.NonMetal.tellurium, 'polonium': Elements.NonMetal.polonium,
                    'nitrogen': Elements.NonMetal.nitrogen, 'phosphorus': Elements.NonMetal.phosphorus,
                    'arsenic': Elements.NonMetal.arsenic, 'antimony': Elements.NonMetal.antimony,
                    'bismuth': Elements.NonMetal.bismuth, 'helium': Elements.NonMetal.helium,
                    'neon': Elements.NonMetal.neon, 'argon': Elements.NonMetal.argon,
                    'krypton': Elements.NonMetal.krypton, 'xenon': Elements.NonMetal.xenon,
                    'radon': Elements.NonMetal.radon}
                    #Add locations of Elements in the inner and outer transition metals

elementSymbol = {'He': elementLocations['helium'], 'Li': elementLocations['lithium'],
                 'Be': elementLocations['beryllium'], 'N': elementLocations['nitrogen'],
                 'O': elementLocations['oxygen'],
                 'Na': elementLocations['sodium'], 'Mg': elementLocations['magnesium'],
                 'P': elementLocations['phosphorus'], 'As': elementLocations['arsenic'],
                 'Sb': elementLocations['antimony'], 'Bi': elementLocations['bismuth'],
                 'F': elementLocations['fluorine'], 'Cl': elementLocations['chlorine'],
                 'Br': elementLocations['bromine'], 'I': elementLocations['iodine'], 'At': elementLocations['astatine'],
                 'Ne': elementLocations['neon'], 'Ar': elementLocations['argon'], 'Kr': elementLocations['krypton'],
                 'Xe': elementLocations['xenon']}