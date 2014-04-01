'''
Created on Dec 6, 2013

@author: thomas
'''

import Elements.Metal
import Elements.NonMetal
import Elements.Hydrogen
import Elements.TransitionMetal

NUMBER_OF_ELEMENTS = 118

singleElementsThatBondToSelf = ["Br", "N", "Cl", "H", "O", "F"]

elementLocations = {'hydrogen': Elements.Hydrogen, 'lithium': Elements.Metal.lithium, 'sodium': Elements.Metal.sodium,
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
                    'radon': Elements.NonMetal.radon,
                    #Transition Metals
                    'scandium': Elements.TransitionMetal.scandium, 'titanium': Elements.TransitionMetal.titanium,
                    'vanadium': Elements.TransitionMetal.vanadium, 'chromium': Elements.TransitionMetal.chromium,
                    'manganese': Elements.TransitionMetal.manganese, 'iron': Elements.TransitionMetal,
                    'cobalt': Elements.TransitionMetal.cobalt, 'nickel': Elements.TransitionMetal.nickel,
                    'copper': Elements.TransitionMetal.copper, 'zinc': Elements.TransitionMetal.zinc,
                    'yttrium': Elements.TransitionMetal.yttrium, 'zirconium': Elements.TransitionMetal.zirconium,
                    'niobium': Elements.TransitionMetal.niobium, 'molybdenum': Elements.TransitionMetal.molybdenum,
                    'technetium': Elements.TransitionMetal.technetium, 'ruthenium': Elements.TransitionMetal.ruthenium,
                    'rhodium': Elements.TransitionMetal.rhodium, 'palladium': Elements.TransitionMetal.palladium,
                    'silver': Elements.TransitionMetal.silver, 'cadmium': Elements.TransitionMetal.cadmium,
                    'hafnium': Elements.TransitionMetal.hafnium, 'tantalum': Elements.TransitionMetal.hafnium,
                    'tungsten': Elements.TransitionMetal.tungsten, 'rhenium': Elements.TransitionMetal.rhenium,
                    'osmium': Elements.TransitionMetal.osmium, 'iridium': Elements.TransitionMetal.iridium,
                    'platinum': Elements.TransitionMetal.platinum, 'gold': Elements.TransitionMetal.gold,
                    'mercury': Elements.TransitionMetal.mercury,'rutherfordium': Elements.TransitionMetal.rutherfordium,
                    'dubnium': Elements.TransitionMetal.dubnium, 'seaborgium': Elements.TransitionMetal.seaborgium,
                    'bohrium': Elements.TransitionMetal.bohrium, 'hassium': Elements.TransitionMetal.hassium,
                    'meitnerium': Elements.TransitionMetal.meitnerium,
                    'darmstadtium': Elements.TransitionMetal.darmstadtium,
                    'roentgenium': Elements.TransitionMetal.roentgenium,
                    'copernicium': Elements.TransitionMetal.copernicium}
                    #Add locations of Elements in the inner and outer transition metals

elementSymbol = {'H': elementLocations['hydrogen'], 'He': elementLocations['helium'], 'Li': elementLocations['lithium'],
                 'Be': elementLocations['beryllium'], 'N': elementLocations['nitrogen'],
                 'O': elementLocations['oxygen'],
                 'Na': elementLocations['sodium'], 'Mg': elementLocations['magnesium'],
                 'P': elementLocations['phosphorus'], 'As': elementLocations['arsenic'],
                 'Sb': elementLocations['antimony'], 'Bi': elementLocations['bismuth'],
                 'F': elementLocations['fluorine'], 'Cl': elementLocations['chlorine'],
                 'Br': elementLocations['bromine'], 'I': elementLocations['iodine'], 'At': elementLocations['astatine'],
                 'Ne': elementLocations['neon'], 'Ar': elementLocations['argon'], 'Kr': elementLocations['krypton'],
                 'Xe': elementLocations['xenon'],
                 #transition metals
                 'Sc': elementLocations['scandium'], 'Ti': elementLocations['titanium'],
                 'V': elementLocations['vanadium'], 'Cr': elementLocations['chromium'],
                 'Mn': elementLocations['manganese'], 'Fe': elementLocations['iron'],
                 'Co': elementLocations['cobalt'], 'Ni': elementLocations['nickel'],
                 'Cu': elementLocations['copper'], 'Zn': elementLocations['zinc'],
                 'Y': elementLocations['yttrium'], 'Zr': elementLocations['zirconium'],
                 'Nb': elementLocations['niobium'], 'Mo': elementLocations['molybdenum'],
                 'Tc': elementLocations['technetium'], 'Ru': elementLocations['ruthenium'],
                 'Rh': elementLocations['rhodium'], 'Pd': elementLocations['palladium'],
                 'Ag': elementLocations['silver'], 'Cd': elementLocations['cadmium'],
                 'Hf': elementLocations['hafnium'], 'Ta': elementLocations['tantalum'],
                 'W': elementLocations['tungsten'], 'Re': elementLocations['rhenium'],
                 'Os': elementLocations['osmium'], 'Ir': elementLocations['iridium'],
                 'Pt': elementLocations['platinum'], 'Au': elementLocations['gold'],
                 'Hg': elementLocations['mercury'], 'Rf': elementLocations['rutherfordium'],
                 'Db': elementLocations['dubnium'], 'Sg': elementLocations['seaborgium'],
                 'Bh': elementLocations['bohrium'], 'Hs': elementLocations['hassium'],
                 'Mt': elementLocations['meitnerium'], 'Ds':elementLocations['darmstadtium'],
                 'Rg': elementLocations['roentgenium'], 'Cn': elementLocations['copernicium']}