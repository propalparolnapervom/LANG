
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










