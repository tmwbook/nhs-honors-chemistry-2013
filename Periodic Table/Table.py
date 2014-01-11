'''
Created on Dec 6, 2013

@author: thomas
'''

import Metal
import NonMetal

NUMBER_OF_ELEMENTS = 118

class Table(object):
    NUMBER_OF_ELEMENTS = 118 #something to stop an error

elementLocations = {'lithium':Metal.lithium,'sodium':Metal.sodium,'potassium':Metal.potassium, 'rubidium':Metal.rubidium,
                    'cesium':Metal.cesium, 'francium':Metal.francium,'beryllium':Metal.beryllium,'magnesium':Metal.magnesium,
                    'calcium':Metal.calcium,'strontium':Metal.strontium,'barium':Metal.barium,'radium':Metal.radium,
                    } #Add locations of Elements in the Metal and NonMetal files