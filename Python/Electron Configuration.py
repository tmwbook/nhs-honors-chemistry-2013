'''
Created on 12 28, 14
 
@author: Thomas
'''
"""
looking to get rid of a lot of the lists, seems like their should be a better way
"""
import Table
 
#Noble Gasses for short hand
He = Table.elementSymbol["He"]
Ne = Table.elementSymbol["Ne"]
Ar = Table.elementSymbol["Ar"]
Kr = Table.elementSymbol["Kr"]
Xe = Table.elementSymbol["Xe"]
#Element not added yet Rn = Table.elementSymbol["Rn"]
#electron configuration with spaces between each sequence
electronConfiguration = ["1s^", "2", " 2s^", "2", " 2p^", "6", " 3s^", "2", " 3p^", "6", " 4s^", "2", " 3d^", "10",
                         " 4p^", "6", " 5s^", "2", " 4d^", "10", " 5p^", "6", " 6s^", "2", " 4f^", "14", " 5d^", "10",
                         " 6p^", "6", " 7s^", "2", " 5f^", "14", " 6d^", "10", " 7p^", "6"]
#Electron Configuration of Noble Gasses
#string version
HeConfiguration = "".join(x for x in electronConfiguration[:2] if x not in "[],'")
NeConfiguration = "".join(x for x in electronConfiguration[:6] if x not in "[],'")
ArConfiguration = "".join(x for x in electronConfiguration[:10] if x not in "[],'")
KrConfiguration = "".join(x for x in electronConfiguration[:16] if x not in "[],'")
XeConfiguration = "".join(x for x in electronConfiguration[:22] if x not in "[],'")
#list version
HeListElements = electronConfiguration[:2]
NeListElements = electronConfiguration[:6]
ArListElements = electronConfiguration[:10]
KrListElements = electronConfiguration[:16]
XeListElements = electronConfiguration[:22]
#List for Noble Gases
nobleGasses = [He, Ne, Ar, Kr, Xe]
nobleGassesStrings = ["He", "Ne", "Ar", "Kr", "Xe"]
nobleGassesConfigurations = [HeConfiguration, NeConfiguration, ArConfiguration, KrConfiguration, XeConfiguration]
nobleGasListElements = [HeListElements, NeListElements, ArListElements, KrListElements, XeListElements]


#should split up this function
def shortHandElectronConfiguration(element):
    global nobleGasses
    elementNumber = Table.elementSymbol[element].atomicNumber
    #i is used to keep track of which noble gas to use for shorthand
    i = 0
    if element.lower() == "h":
        return "1s^1"
    for gas in nobleGasses:
        if not elementNumber >= gas.atomicNumber:
            gasForShortHand = "[" + nobleGassesStrings[i - 1] + "]"
            elementConf = findElectronConfiguration(element)
            strippingFrontOfConf = len(nobleGassesConfigurations[i - 1])
            fullShortHand = gasForShortHand + elementConf[strippingFrontOfConf:]
            return fullShortHand
        else:
            i += 1
 
 
def findElectronConfiguration(element):
    elementConfiguration = ""
    for part in electronConfiguration:
        if element.lower() == "h":
            elementConfiguration = '1s^1'
            break
        elif part == Table.elementSymbol[element].lastElectConf[0]:
            elementConfiguration += "".join(x for x in Table.elementSymbol[element].lastElectConf if x not in "[]")
            break
        else:
            elementConfiguration += part
    return elementConfiguration