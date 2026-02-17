with open('Files/fruits.txt', 'a+') as file:
    file.seek(0)
    rd1 = file.read()
    file.write(rd1)
    file.write(rd1)