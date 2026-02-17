from app import app
import random

@app.route('/')
@app.route('/index')


def index():

    list2 = ["Spiderman", "Superman", "Batman", "Iron Man", "Hulk", "Flash", "Aquaman", "Hawkeye", "Wolverine"]
    randomhero = random.choice(list2)
    #return "Your Superhero is: " + randomhero
    if randomhero != "Spiderman":
        return "Sorry, " + randomhero + "" + " You lose!"
    else:
        return "You chose " + randomhero + "You win!"


#def index():
    #return "Welcome to your first app built with Flask."