
# Get a list of list
# [
#   [.,.,0],
#   [0,0,0],
#   [.,.,0],
# ]
# Rotate it on 90 degrees
#   .0.
#   .0.
#   000


grid = [
    ['O', 'O','O','O'],
    ['.', '.','.','O'],
    ['O', 'O','O','O'],
    ['.', '.','.','O'],
    ['.', 'O','.','O'],
]

def rotateGrid(gridToRotate):

    # Number of sub-lists in the original list
    sublists = len(gridToRotate)

    # Number of items in each sublist (1st one, for example)
    sublistItems = len(gridToRotate[1])

    for x in range(sublistItems):

        newLine = ''

        for y in range(sublists):

            newLine = newLine + str(gridToRotate[y][x])

        # Print reversed line (in other case, it will be mirrored to correct one)
        print(newLine[::-1])



print('\n   Original grid:  \n')
for g in range(len(grid)):
    print(grid[g])

print('\n   Converted grid:  \n')
rotateGrid(grid)
