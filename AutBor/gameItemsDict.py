
inventoryList = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(k, v) 
    print('Total number of items: ' + str(item_total))


# displayInventory(inventoryList)

# add items from a list (dragonLoot) into a dictionary (inv)

def addToInventory(inventory, addedItems):
    # loop over each item in dragonLoot
    for i in addedItems:
        # if item exists as a key in inv.keys(), then add 1 to the dictionary key inventory[i]
        if i in inventory.keys():
            inventory[i] += 1
        # otherwise add it to the dictionary as a key-value pair with a value of 1
        else:
            inventory[i] = 1
    return inventory
   
    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print(inv)

displayInventory(inv)
