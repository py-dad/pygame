import random
messages = ['Thank you!',
            'Im running late',
            'cant talk now',
            'text me',
            
            'let\'s do lunch',
            'busy',
            'call you back',
            'see you soon',
            'on my way'
            ]

print(messages[random.randint(0, len(messages)- 1)])
print(len(messages))