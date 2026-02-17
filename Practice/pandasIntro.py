import pandas as pd

# basic dataframe
mydataset = {
    'cars': ["BMW", "VOLVO", "FORD"],
    'passings': [3,7,2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# verison check -> print(pd.__version__)

# a Panda series is like a column in a table

a = [1, 7, 2]

myvar =pd.Series(a)
print(myvar)

# with the index arg, you can name your own labels

myvar = pd.Series(a, index = ['x', 'y', 'z'])

print(myvar)

# you can also use key/value objects (like dictionary), when creating a Series
# you can also use index to specify only the items to include in the Series

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
print(myvar)

