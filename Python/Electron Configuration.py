'''
Created on 12 28, 14

@author: Thomas
'''
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
HeConfiguration = "".join(x for x in electronConfiguration[:2] if x not in "[],'")
NeConfiguration = "".join(x for x in electronConfiguration[:6] if x not in "[],'")
ArConfiguration = "".join(x for x in electronConfiguration[:10] if x not in "[],'")
KrConfiguration = "".join(x for x in electronConfiguration[:16] if x not in "[],'")
XeConfiguration = "".join(x for x in electronConfiguration[:22] if x not in "[],'")


def findElectronConfiguration(element):
    pass