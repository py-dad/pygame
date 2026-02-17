import pygame

#playing around with classes

class Test():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #print(f'age is {age} name is {name}')

    def ageInTen(self):
        older = int(age) + 10
        print(f'age in 10 is {older}')

   

age = input('enter age: ')
name = input('enter name: ')

guy = Test(name, age)

guy.ageInTen()



