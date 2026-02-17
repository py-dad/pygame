import random
secretNumber = random.randint(1,20)

print('I am thinking of a nubmer between 1 and 20')

# Give player six chances to guess.

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess > secretNumber:
        print('guess too high')
    elif guess < secretNumber:
        print('guess too low')
    else:
        break  # This condition is the correct guess

if guess == secretNumber:
    print('Good job! you guessed my number in '+ str(guessesTaken) + ' tries!')
else:
    print('Nope. The number i was thinking of was ' + str(secretNumber))