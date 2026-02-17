import time

print('How old is Bryson?')
time.sleep(1.5)
print('A. 6')
time.sleep(1.5)
print('B. 8')
time.sleep(1.5)
print('C. 4')
time.sleep(1.5)
print('D. 7')
time.sleep(2)

run = True

while run:
    choice = input('Enter your choice: ').upper()

    if choice == 'D':
     print('Congratulations! You are correct.')
     break

    else: 
        print('That is not correct. Try again.')
        time.sleep(1.5)
