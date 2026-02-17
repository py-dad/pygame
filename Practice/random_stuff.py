#random superhero game
import random



list2 = ["Spiderman", "Superman", "Batman", "Iron Man", "Hulk", "***Flash***", "Aquaman", "Hawkeye", "Wolverine"]
randomhero = random.choice(list2)
print("Your superhero is: " + randomhero)

if randomhero != "***Flash***":
    print("Sorry, you lose to the Joker!!!")
else:
   print(randomhero + ", You have saved the city! Congratulations!")
   



