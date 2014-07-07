'''
@author: Thomas
'''
# M = moles solute / liters


def calculateMolarity():
    molesSolute = float(raw_input('How many moles of the solute do you have?' ))
    litersSolvent = float(raw_input('How many liters of the solvent do you have? '))
    return float(molesSolute) / float(litersSolvent)


def calculateLiters():
    molarity = float(raw_input('What is the molarity of the solution? '))
    molesSolute = float(raw_input('How many moles are there dissolved in the solute? '))
    return molesSolute / molarity


def calculateMoles():
    molarity = int(raw_input('What is the molarity of the solution? '))
    litersSolvent = float(raw_input('How many liters of the solvent do you have? '))
    molesSolute = molarity * litersSolvent
    return molesSolute


def setBool(a):
    if a.lower() == 'y':
        return True
    else:
        return False


def typeOfProblem():
    molesCheck = raw_input('Do you know the amount of moles in the solution?(y/n) ')
    litersCheck = raw_input('Do you know the amount of liters in the solution?(y/n) ')
    molesCheck = setBool(molesCheck)
    litersCheck = setBool(litersCheck)
    if molesCheck and litersCheck:
        print "M = " + str(calculateMolarity())
    elif molesCheck and not litersCheck:
        print str(calculateLiters()) + " L"
    else:
        print str(calculateMoles()) + " mol"

if __name__ == "__main__":
    while True:
        typeOfProblem()
        option = raw_input('Do you need to solve another problem?(y/n) ')
        if option.lower() == "y":
            continue
        else:
            break