'''
Created on Dec 6, 2013

@author: thomas
'''

import Elements.Metal
import Elements.NonMetal
import Elements.Hydrogen
import Elements.TransitionMetal
import Elements.Lanthanide
import Elements.Actinide

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
                    'copernicium': Elements.TransitionMetal.copernicium,
                    #Lanthanoid locations
                    'lanthanum': Elements.Lanthanide.lanthanum, 'cerium': Elements.Lanthanide.cerium,
                    'praseodymium': Elements.Lanthanide.praseodymium, 'neodymium': Elements.Lanthanide.neodymium,
                    'neodymium': Elements.Lanthanide.neodymium, 'promethium': Elements.Lanthanide.promethium,
                    'samarium': Elements.Lanthanide.samarium, 'europium': Elements.Lanthanide.europium,
                    'gadolinium': Elements.Lanthanide.gadolinium, 'terbium': Elements.Lanthanide.terbium,
                    'dysprosium': Elements.Lanthanide.dysprosium, 'holmium': Elements.Lanthanide.holmium,
                    'erbium': Elements.Lanthanide.erbium, 'thulium': Elements.Lanthanide.thulium,
                    'ytterbium': Elements.Lanthanide.ytterbium, 'lutetium': Elements.Lanthanide.lutetium,
                    #Actinide locations
                    'actinium': Elements.Actinide.actinium, 'thorium': Elements.Actinide.thorium,
                    'protactinium': Elements.Actinide.protactinium, 'uranium': Elements.Actinide.uranium,
                    'neptunium': Elements.Actinide.neptunium, 'plutonium': Elements.Actinide.plutonium,
                    'americium': Elements.Actinide.americium, 'curium': Elements.Actinide.curium, 
                    'berkelium': Elements.Actinide.berkelium, 'californium': Elements.Actinide.californium,
                    'einsteinium': Elements.Actinide.einsteinium, 'fermium': Elements.Actinide.fermium, 
                    'mendelevium': Elements.Actinide.mendelevium, 'nobelium': Elements.Actinide.nobelium,
                    'lawrencium': Elements.Actinide.lawrencium}

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
                 'Mt': elementLocations['meitnerium'], 'Ds': elementLocations['darmstadtium'],
                 'Rg': elementLocations['roentgenium'], 'Cn': elementLocations['copernicium'],
                 #Lanthanides
                 'La': elementLocations['lanthanum'], 'Ce': elementLocations['cerium'],
                 'Pr': elementLocations['praseodymium'], 'Nd': elementLocations['neodymium'],
                 'Pm': elementLocations['promethium'], 'Sm': elementLocations['samarium'],
                 'Eu': elementLocations['europium'], 'Gd': elementLocations['gadolinium'],
                 'Tb': elementLocations['terbium'], 'Dy': elementLocations['dysprosium'],
                 'Ho': elementLocations['holmium'], 'Er': elementLocations['erbium'], 
                 'Tm': elementLocations['thulium'], 'Yb': elementLocations['ytterbium'],
                 'Lu': elementLocations['lutetium'],
                 #Actinide
                 'Ac': elementLocations['actinium'], 'Th': elementLocations['thorium'],
                 'Pa': elementLocations['protactinium'], 'U': elementLocations['uranium'],
                 'Np': elementLocations['neptunium'], 'Pu': elementLocations['plutonium'],
                 'Am': elementLocations['americium'], 'Cm': elementLocations['curium'], 
                 'Bk': elementLocations['berkelium'], 'Cf': elementLocations['californium'],
                 'Es': elementLocations['einsteinium'], 'Fm': elementLocations['fermium'],
                 'Md': elementLocations['mendelevium'], 'No': elementLocations['nobelium'],
                 'Lr': elementLocations['lawrencium']}

i = 0
for x in elementLocations:
    i+= 1
print i