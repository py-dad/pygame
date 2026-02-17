import random, time, copy


WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:

nextCells = []

for x in range(WIDTH):
    column = [] # create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') # add a living cell

