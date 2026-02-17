#! python3

# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard
# Note some zip codes may make a partial match
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   #area code with or without parentheses
    (\s|-|\.)?     #separator
    (\d{3})    #first 3 digits
    (\s|-|\.)  #separator
    (\d{4})    #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension \s* accounts for any number of spaces
)''', re.VERBOSE)

#TODO: Create email regex
emailRegex = re.compile (r'''(
    [a-zA-Z0-9._%+-]+   #username
    @       # @ symbol
    [a-zA-Z0-9.-]+   #domain name
    (\.[a-zA-z]{2,4})   #dot-something
)''', re.VERBOSE)

#TODO: Find matches in clipboard text

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) #put in consistent format with - between matches
    if groups[8] != '':
        phoneNum += '  x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


#TODO: Copy results to clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches)) #joins matches with new lines (better format)
else:
    print('No phone numbers of email addresses found.')

