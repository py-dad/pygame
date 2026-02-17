# error handling
'''When code in a try clause causes an error, 
the program execution immediately moves to the code in the except clause.'''
def spam(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print("Err. you caint dahvide by 0.")


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

#if there is an exception...
#program will continue moving down instead of jumping back up to Try again
print('does the progam still execute after an error?')


