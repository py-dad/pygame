
#random basics in AutBor

#import multiple modules in a single import statement
import random, sys, os, math

for i in range(0,10):
    #Since randint() is in the random module, you must first type random
    print(random.randint(15,100))



#for loop basis in AutBor
'''for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')


    #add up all numbers from 0 to 100

    total = 0

for num in range(101):

    total = total + num
    print('(total = ' + str(total) + ') (num = ' + str(num) + ')')

    #more efficent way to code the expression
    #total += num
print(total)


i = 0

while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i += 1
#The first argument will be where the for loop’s variable starts, 
#and the second argument will be up to, but not including, the number to stop at.
for i in range(12,16):
    print(i)

#start, stop, and step (increase at each interval)
for i in range(0,502,2):
    print(i)

#you can even use a negative number to make the for loop count down instead of up
#first arg must be higher than second, or else you cannot count down  
for i in range(50,0, -1):
    print(i)'''