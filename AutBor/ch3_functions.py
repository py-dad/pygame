import random


def getAnswer(answerNumber):
    print('let\'s see if you\'ve won')

    if answerNumber == 1:
        return 'a dream vacation!'
    
    elif answerNumber == 2:
        return 'a new car!'
    
    elif answerNumber == 3:
        return 'shopping spree!'
    
    elif answerNumber == 4:
        return 'a home makeover!'
    
    elif answerNumber == 5:
        return 'sorry, you didnt\'t win'
    

""" r = random.randint(1,5)
result = getAnswer(r)
print(result)
 """
# could shorten to one line
# a function call can be used in an expression b/c the call evaluates to its return value 
print(getAnswer(random.randint(1,5)))





















""" def hello():
    print("howdy!")
    print('howdy!!')
    print('Hello There')

hello()
hello()
hello() """

#basic
""" def hello(name): <-- create/define function; name is parameter
    print('Hello, '+ name)

hello('Alice') <-- call function, pass argument 'Alice' to function

# using variables for agrument
def helloNei(name):
    print('Hello, ' + name)


name = input("enter name: ")

helloNei(name)
 """