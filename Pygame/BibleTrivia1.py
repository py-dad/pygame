import time

print('How old was Methusaleh?')
time.sleep(1.5)
print('A. 169')
time.sleep(1.5)
print('B. 444')
time.sleep(1.5)
print('C. 969')
time.sleep(1.5)
print('D. 966')
time.sleep(2)

run = True

while run:
    choice = input('Enter your choice: ').upper()

    if choice == 'C':
     print('Congratulations! You are correct.')
     break

    else: 
        print('That is not correct. Try again.')
        time.sleep(1.5)