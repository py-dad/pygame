import time

print('How old was Moses?')
time.sleep(1.5)
print('A. 169')
time.sleep(1.5)
print('B. 620')
time.sleep(1.5)
print('C. 120')
time.sleep(1.5)
print('D. 210')
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

print('Round 2')

print('How old was Noah?')
time.sleep(1.5)
print('A. 169')
time.sleep(1.5)
print('B. 620')
time.sleep(1.5)
print('C. 120')
time.sleep(1.5)
print('D. 950')
time.sleep(2)

run = True

while run:
    choice = input('Enter your choice: ').upper()

    if choice == 'D':
     print(''''Congratulations! You are correct. The Bible says Noah lived to be 950
           years old!''')
     break

    else: 
        print('That is not correct. Try again.')
        time.sleep(1.5)