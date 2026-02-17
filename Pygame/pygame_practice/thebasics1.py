
# https://pyga.me/docs/tutorials/en/move-it.html

# Create separate copy of the screen background to track original values
background = [1, 1, 2, 2, 2, 1]

screen = [0]*6 # a new blank screen. create new list with 6 0s
print(screen)       
for i in range(6):
    screen[i] = background[i]


screen = [1, 1, 2, 2, 2, 1]
print(screen)

#screen[3] = 8
#print(screen)

playerpos = 3
#screen[playerpos] = 8
#print(screen) 
 
# playerpos starts with a value of 3
#playerpos = playerpos - 1
# playerpos value now 2
# reference index 2 and insert the value 8
#screen[playerpos] = 8
# he's basically moving the 8 from index 3 to index 2, while leaving
# the original 8 in index 3 (old position)
#print(screen)

# reset screen values back to original values
screen[playerpos] = background[playerpos]
playerpos = playerpos -1
screen[playerpos] = 8
print(screen)





