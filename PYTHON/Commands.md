

## Functions: Built-in
[Docs](https://docs.python.org/3/library/functions.html)

### range

Start range from 0, got up to 6 (not including), with step of 2
```
for i in range(0,6,2):
    print(i) 
```

## Functions: Custom

### Without arguments

```
# Define function wo arguments
def hello():
    print('Hello')
    print('How are you?')

# Call function wo arguments
hello()
```

### With arguments

```
# Define function w arguments
def hello(name):
    print('Hello, ' + name)

# Call function w arguments
hello('Serg')
```

### With arguments and return
```
import random

# Define function w arguments and return
def insert_name_get_answer(name):
    if name == 'serg':
        return 'The best name ever'
    else:
        return 'It is good one too'
    
# Pickup random name from the list
randomName=random.choice(['serg', 'marta', 'kiril'])

print('What about ' + randomName + '?')

# Call function w arguments
returnedAnswer=insert_name_get_answer(randomName)

print(returnedAnswer)
```

## Modules
[Docs](https://docs.python.org/3/py-modindex.html)

### random

Random integer, from 1 to 9
```
import random

randomNumber = random.randint(1,9)
print(str(randomNumber))
```

Random item from the array
```
import random

randomName = random.choice(['serg', 'marta', 'kiril'])
print(randomName)
```

### sys

Exit, with specific status
```
import sys

print('Name:')
name = input()

if name == 'serg':
    print('Exiting')
    sys.exit(3)
```

## Exceptions Handling

[Docs: Built-In Exceptions](https://docs.python.org/3/library/exceptions.html#built-in-exceptions)

Some pre-defined built-in exceptions and overall one (for all other cases?):
```
def dividing(numToDel):
    try:
        return 13 / numToDel
    except ZeroDivisionError:
        print('   ERR: You can no delete on this number: ' + str(numToDel))
    except TypeError:
        print('   ERR: This should be number: ' + str(numToDel))
    except:
        print('   ERR: Undefined reason, but you can not do like this.')


print(dividing(1))
print(dividing(0)) # Division by 0
print(dividing(13))
print(dividing('serg')) # Division on wrong type (string)
print(dividing(1))
```

Show that try: -> except: transition is implemented just after very first error in the try: block (if any):
```
def dividing(numToDel):
    return 13 / numToDel

try:
    print(dividing(1))
    print(dividing(0)) # Division by 0 ERROR
    print(' LOOK AT ME!!!')
except:
    print('  ERR: Something went wrong')

print('\nAs you can see, steps from try: block are ommited after very first error')
print('This is because try -> except transition is implemented just after first error \n')
```


## Types: Overall

### Lists

Input list items from the dialogue:
```
# Define list variable
cats = []

while True:
    print('Input name of the cat (or leave it empty to finish the list)')
    name = input()

    # Finish input once item from the input is empty
    if name == '':
        break

    # Add new item to the list
    cats = cats + [name]

print('\nSo you have mentioned following cats:')

for catName in cats:
    print(catName)


```

Work simultaneously with both 'list index' and corresponding 'list value'
```
# Define list variable
cats = ['barsik', 'murka', 'persik']

# Work with both 'index number' and corresponding 'list value'
for i in range(len(cats)):
    print('The list item number ' + str(i) + ' is: ' + cats[i])
```

Is item in the list?
```
# Define list variable
hardcodedListOfCats = ['barsik', 'murka', 'persik']

print('Enter any name of the pet')
suggestedPetName = input()

# Is your name in the list?
if suggestedPetName in hardcodedListOfCats:
    print('Yup, you are right.')
else:
    print('Nope, there is no such name in the hardcoded list')
```


Set multiple variables from the list
```
# Define list with some characteristics
barsikTheCat = ['grey', 'loud', 'heavy']

# Set variables, which value corresponds 
# to items from the list
#
# NB: The variables number should be the same as list's items number
barsikColor, barsikVolume, barsikWeight = barsikTheCat

# Verify it
print('Barsiks color is: ' + barsikColor)
print('Barsiks volume is: ' + barsikVolume)
print('Barsiks weight is: ' + barsikWeight)
```

List of the lists:
```
grid = [
    [10,11,12],
    [20,21,22],
    [30,31,32]
]

print('Should be 10:  ' + str(grid[0][0]))
print('Should be 21:  ' + str(grid[1][1]))
print('Should be 32:  ' + str(grid[2][2]))
```

### Strings

> NB: Might be handled like `list`, but immutable

Show first 4 "items" only
```
>>> name = 'sergii'
>>> name[0:4]
'serg'
```


### Tuples

> NB: Same as `list`, but immutable. 
> Use `()` instead of `[]`

Show 2nd item in the tuple
```
>>> cats = ('barsik', 'koko')
>>> cats[1]
'koko'
```

### Dictionaries

```
import pprint

# Initialize empty dictionary
count = {}

# If the `symbol` is not present in the dictionary yet,
# use `setdefault` method to add it, with value `0`
count.setdefault('symbol', 0)

print(count)

# # Uncomment for nice look
# pprint.pprint(count)
```


## Types: Convertation

### Define current type

```
>>> type('koko')
<class 'str'>

>>> type(0.24)
<class 'float'>

>>> type(24)
<class 'int'>
```

### To String

Integer -> String
```
>>> str(24)
'24'
```

### To Integer

String -> Integer
```
>>> int("43")
43
```

### To List
Tuple -> List
```
>>> list(('barsik', 'koko'))
['barsik', 'koko']
```

String -> List
```
>>> list('barsik')
['b', 'a', 'r', 's', 'i', 'k']
```

### To Tuple

List -> Tuple
```
>>> tuple(['barsik', 'koko'])
('barsik', 'koko')
```

String -> Tuple
```
>>> tuple ('barsik')
('b', 'a', 'r', 's', 'i', 'k')
```






