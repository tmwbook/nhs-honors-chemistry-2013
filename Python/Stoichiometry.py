'''
Created on Nov 21, 2013

author: Thomas
'''
from sys import exit
import Table


def molesToGrams(moles, molarMass):
    grams = moles * molarMass
    return grams


def gramsToMoles(grams, molarMass):
    answer = grams / molarMass
    return answer


def stoichiometry(step):
    coefficientA = float(raw_input('What is the coefficient of the element/compound we have information for?'))
    coefficientB = float(raw_input('What is the coefficient of the element/computnd we do not have information for?'))
    answer = coefficientB * step / coefficientA
    return answer


def elementOrCompund():
    answer = raw_input("Is the first item an element or a compound? (e/c)")
    if answer.lower() == "e":
        getGramsInElement()
    else:
        calculateGramsInCompound()


def getGramsInElement():
    element = raw_input("What is the symbol for the first element you are using? (case sensitive)")
    return Table.elementSymbol[element].atomicMass


def calculateGramsInCompound():
    pass

def mainProgram():
    problemOption = raw_input('Are you starting with grams?(y/n)')
    if problemOption == 'y' or problemOption == 'Y':
        """
        molarMassA = float(raw_input('What is the molar mass of the element/compound that we have inforation for?'))
        grams = float(raw_input('How many grams of the element/compound do you have?'))
        """

        option = raw_input('Do you need to convert to grams after stoichiometry?(y/n)')
        threeStepsGrams = stoichiometry(gramsToMoles(grams, molarMassA))
        if option.lower() == 'y':
            molarMassB = float(raw_input('What is the molar mass of the element/compound that we are trying to figure out?'))
            print "The final answer is " + str(molesToGrams(threeStepsGrams, molarMassB)) + " gram(s)."
            runAgain()
        else:
            print "The final answer is " + str(threeStepsGrams) + " mole(s)."
            runAgain()
    else:
        moles = float(raw_input('How many moles of the element/compound are we starting with?'))
        twoStepMoles = stoichiometry(moles)
        optionMoles = raw_input('After stoichiometry, do we need to convert to grams?(y/n)')
        if optionMoles == 'y' or optionMoles == 'Y':
            molarMassB = float(raw_input('What is the molar mass of the element/compound that we are trying to figure out?'))
            print "The final answer is " + str(molesToGrams(twoStepMoles, molarMassB)) + " gram(s)"
            runAgain()
        else:
            print "The final answer is " + str(twoStepMoles) + " mole(s)"
            runAgain()

def runAgain():
    reRunOption = raw_input('Would you like to solve another problem? (y/n)')
    if reRunOption == 'y' or reRunOption == 'Y':
        mainProgram()
    else:
        exit()


if __name__ == '__main__':
    mainProgram()