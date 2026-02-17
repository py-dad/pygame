def printTable(tableData):
    # Initialize colWidths with zeros
    colWidths = [0] * len(tableData)

    # Find the maximum width of each column
    for i in range(len(tableData)):
        print(f' value of i: {i}')
        for item in tableData[i]: # iterate over each inner list
            print('Value of tableData[i]: ' + str(tableData[i]))
            colWidths[i] = max(colWidths[i], len(item))
            print(f'Value of colWidths: {colWidths}')

    # Print the table
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print()  # Move to the next line after printing each row

# Example usage:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
