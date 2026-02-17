with open('Files/vegetables.txt', 'w') as myFile:
    myFile.write("Tomato\nCucumber\nOnion\n")
    myFile.write('Garlic')



# print first 90 characters of bear.txt
with open('Files/bear.txt') as file:
    content = file.read()

print(content[:90])

