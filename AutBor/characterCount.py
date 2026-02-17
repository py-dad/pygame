import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen. '

count = {}

for character in message:
    # set each character defaul value to 0, so
    # can be counted correctly
    count.setdefault(character, 0)
    # add 1 each time it is seen in the loop
    count[character] = count[character] + 1

#pprint.pprint(count)
    
    # or

print(pprint.pformat(count))