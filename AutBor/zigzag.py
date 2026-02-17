import time, sys

indent = 0 # how many spaces to indent

indentIncreasing = True #whether the indention is increasing or now

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.01) #pause for 1/10 of second

        if indentIncreasing:
            # Increase the number of spaces:
            indent += 1

            if indent == 20:
                #change direction
                indentIncreasing = False

        else: 
            # decrease the number of spaces

            indent -= 1
            if indent == 0:
                #change direction
                indentIncreasing = True

#except statement
except KeyboardInterrupt:
    sys.exit()

