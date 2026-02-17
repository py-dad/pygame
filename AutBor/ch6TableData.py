def printTable(tableData):
    # Initialize colWidths with zeros for each column
    colWidths = [0] * len(tableData)

    # Find the maximum width for each column
    for row in tableData:
        for colIndex, cell in enumerate(row):
            colWidths[colIndex] = max(colWidths[colIndex], len(cell))

    # Print the table
    for row in tableData:
        for colIndex, cell in enumerate(row):
            # Right-justify each cell using rjust()
            print(cell.rjust(colWidths[colIndex]), end=' ')
        print()  # Move to the next row

# Example usage
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
