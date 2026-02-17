
# Pretty Challenging Example from AutBor chapter 6 TablePrint
# throwing errors even using direct examples from the web?


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


num_of_lists = len(tableData) # = 3 lists
# since all lists have the same number of items,
# grab the number/len from the first list
items_in_list = (len(tableData[0])) # returns 4 items

#empty list to hold value of the inner string in each inner list
max_length_list = [] 

for list in tableData:
    max_length_item = 0 # variable for longest string of each list
    #change value only if the new list for len(item) is greater than previous
    for item in list:
        if len(item) > max_length_item:
            max_length_item = len(item)
    max_length_list.append(max_length_item)
    print(max_length_list)

    #print the results. we want a total of 4 rows and 3 columns
    #the first loop iterates over each row, so we use items_in_list
    #since there are 4 items in each inner list

# the second loop iterates over columns, so we use num_of_lists,
#since that is ewqual to how many columns we want
#we use rjust formatting, as exmample explained
#we need to iterate through each item in the max_length_list
#since we are justifying 3 different columns, we use
#the row iterator from num_of_lists.
#last we want to space out each word, so use end=' ' after each
#print directly, but add print('') afger the first for loop finishes
#so you can print the next line


    for row in range(items_in_list):
        for col in range(num_of_lists):
            print(tableData[col][row].rjust(max_length_list[col], end = ' '))
            print('')