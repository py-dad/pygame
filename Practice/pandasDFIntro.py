import pandas as pd

# Data sets in Pands are usually multi-dimensional tables, called DataFrames

data = {"calories": [420, 380, 390],
        "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)

# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns

# Pandas use the loc attribute to return one or more specified row(s)

print(f'locate a row: {df.loc[0]}')

# returns a Panda series
print(df.loc[[0,2]])

# you can name your indexes with the index argument

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index= ["day1", "day2", "day3"])

print(df)

# loc attribute can return specified row(s)
print(df.loc["day2"])