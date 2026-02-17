#use range (another type of object)
#student_grades = [0,11]

#convert to list

student_grades = list(range(0,11))

#prints same list 3 times
#print(student_grades * 3)

#print(type(student_grades))
print(student_grades)

#example of a method called upper
#methods take parenthesis 

#print is a function, no dot required. example print(1)
print("hello".upper()) # = HELLO
print("hello".title()) # = Hello

myword = input("Please enter your name: ")
print(myword.title())

#more function examples 
mysum = sum(student_grades)
length = len(student_grades)

#mean calculation since there is no mean function 

mean = mysum / length

print(mean)