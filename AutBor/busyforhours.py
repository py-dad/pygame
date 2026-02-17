import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt) #only accepts a yes/no repsponse

    if response == 'no':
        break 
print('Thank you. Have a nice day.')