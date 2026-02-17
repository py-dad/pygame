

catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1 ) +
    ' (Or enter nothing to stop.):')
    

    name = input()

    if name == '':
        break

    # list concatenation. note: variable name must be in [] to declare
    # as a list so it can be concatenated to other list [catNames]
    catNames = catNames + [name] 

print('The cat names are: ')

for name in catNames:
    print(' ' + name)