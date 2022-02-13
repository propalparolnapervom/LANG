####################################
# Get list [a, b, c]
# Convert it to string 'a, b and c'
####################################

import copy

# Define list with some characteristics
cats = ['barsik', 'koko', 'murka', 'lala', 'roro']

# Define function to work with List
def convertList (listToString):
    providedList = copy.copy(listToString)

    lengthOfProvidedList = len(providedList)

    firstPart = ''
    for i in range(lengthOfProvidedList - 1):
        firstPart = firstPart + cats[i] + ', '

    firstPart = firstPart[:len(firstPart)-2]
    
    secondPart = providedList[-1]

    print('   Provided:')
    print(cats)

    print('   Converted:')
    print(firstPart + ' and ' + secondPart)


# Call the function
convertList(cats)
