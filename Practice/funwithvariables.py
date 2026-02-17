username = input("Enter your name: ")
#print("Hi, "+ username.title() + "!")

#get length (number of characters in name)
nameLen = len(username)

#fun little conditional statement 
while username == "":
    print("What, no name?: ")
    username == ("Try entering your name again: ")

print ("Your name has " + str(nameLen) + " letters.")



#return the size of the string in memory, in bytes
size = username.__sizeof__()

print(str(size) + "bytes")