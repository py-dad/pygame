temps = [221, 234, 340, 230]

#put code inline in the new list
new_temps = [temp / 10 for temp in temps]

print(new_temps)



temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 for temp in temps if temp != -9999]
print(new_temps)