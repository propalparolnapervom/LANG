
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



