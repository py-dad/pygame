#example with if statment, it doesn't loop

spam = 0
if spam < 5:
    print('Hello, World')
    spam = spam +1

#example with while statement, it does loop
while spam < 5:
    print("hello world")
    spam = spam + 1

#another example of something like printing mailing labels
counter = 0
#must convert user input to int in order to add to spam variable
words = input("Enter your address: ")
number = int(input('Enter number of labels: '))

#while loop executes print function until 
# counter must be less than number to get accurate number of prints
# if counter were <= number, then it would print out 1 too many 
while counter < number:
    print(words)
    counter = counter + 1

#annoying while loop
    
name = ''
while name != "your name":
    print('please type your name')
    name = input()
print("the loop is closed")

#break statement, similar to above, but uses break to exit loop
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('you have exited the while loop')

#While loop with continue statement

while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        continue
    print("hello, joe. what is the password? (it is a fish)")
    password = input()
    if password == "swordfish":
        break
print("access granted")