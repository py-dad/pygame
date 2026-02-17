import random

#list.append adds to EOL, list.insert lets you add to a specific position (index)
#entry = input("Enter an anmial")
list = ["Turkey", "Larva", "Shark", "Penguin","Wild Tugar","Lion","Camel"]
#list.append(entry)
#print(list)
#randomlist = "You are an: " + str(random.choices(list))

#playing around with the loop
key = ''
counter = 0
while key != 'q':
    key = input('Press Enter to See Your Animal...')
    randomlist = "You got a: " + str(random.choices(list))
    print(randomlist)
    counter = counter + 1
    #print(counter)
    if counter > 20:
        print("Press Q to Quit")
    
