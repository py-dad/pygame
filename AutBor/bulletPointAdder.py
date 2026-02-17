#! python 3
# bulletPointAdder.py - Adds wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

print(text)
# TODO: Separate lines and add stars

pyperclip.copy(text)

lines = text.split('\n')

for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

print(lines)
text = '\n'.join(lines)

pyperclip.copy(text)
print(text)
