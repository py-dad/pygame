#creating a class of my own

#a class is a key element of OOP. use it to create many instances or objects that have similar attributes
#you can also define functions within class to run on said instances

class Boss:
    def __init__(self, name, hits, weapons, speed):
        self.name = name
        self.hits = hits
        self.weapons = weapons
        #you can add a string to these variables
        self.speed =  "Speed =  "  + str(speed)


    # create a function
    def traits(self):
        return '{} {}'.format(self.name, self.hits)

#create variables for user input (optional, just testing)
nme = input("Enter value for name: ")
hts = input("enter boss's hits: ")
wps = input("Enter weapon: ")
spd = input("Enter speed: ")

#create instance **Make sure you place the CLASS name before the tuple**
#also Make Sure you pass the required number of args as defined in Class
boss_1 = Boss("Dr. Wiley", 3, "fire", 25)

boss_2 = Boss(nme, hts, wps, spd)


print(Boss.traits(boss_2)) #variables assigned by user input
print(Boss.traits(boss_1)) #variables set by coder 

print(boss_1.weapons)

        
    