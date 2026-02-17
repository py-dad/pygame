# reverse word

def reverse_word(word):
   if not isinstance(word, (str)):
        return "Input must be a string!"
   else:
       word = word[::-1]
       return word
  


reverse_word("remember")


def rword(wrd):
    return wrd[::-1] if isinstance(wrd, str) else print("Input must be a string")

rword('stairs')

# celisus to to farenheit converter
# If the input is not a number, return "Invalid temperature input".
def c_to_f(temp_c):
    if not isinstance(temp_c, (int, float)):
        return "Invalid Entry -- not a number"
    else:
        return (temp_c * 9/5) + 32

ui = input("please enter a celsius value: ")

try:
    ui = float(ui)
except:
    ui = ui
temp_f = c_to_f(ui)
print(temp_f)

# odd or even function
# The return hands the value back like a secret note 
# The print is what actually yells it out
def odd_or_even(num):
    if not isinstance(num, (int)):
        return "Invalid Entry"
    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')

odd_or_even("string")


# double the number function

def double_number(num):
    dbl = num * 2
    print(dbl)


double_number(17)

# Now with input validation 

def double_number_i(num):
    if not isinstance(num, (int, float)):
        print('Invalid Input! Must be a number')
    else:
        dbl = num * 2
        print(dbl)

double_number_i("dog")

# Simple Functions
# Use return to store result as variable for later use in another function, etc. 

def get_discounted_price(price):
    return price * 0.9  # returns 10% off

new_price = get_discounted_price(100)
print(f"Discounted price is ${new_price}")

get_discounted_price(9)

def namePrt(name="dude"):   # Note default value is "dude" if no value entered
    return f'Hi, there, {name}' # Stores result of namePrt(name)

greet = namePrt() # Assigns result of namePrt() to the var greet
print(greet) # Prints greet variable