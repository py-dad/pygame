#create some functions

#define what the function will do, and what parameters it will take
def mean (mylist):
    the_mean =sum(mylist) / len(mylist)
    return the_mean

mylist = [1,5,7,9]
#call the mean function on the mylist variable
print(mean(mylist))



#call the function, making sure to pass in a paramter as notated in definition
#the mylist parameter (defined above) doesn't have to be a list, it can be any data type
#the mylist parameter is essentially a placeholder for an argument during the function call

#print(mean([1, 4, 5]))

def addit(num1,num2):
    total = num1 + num2
    return total

#print(addit(5,2))

