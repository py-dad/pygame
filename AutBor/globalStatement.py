
# global statement used by function
# to reference variable at global scope

def spam():
    global eggs
    eggs = 'spam'


eggs = 'global'


spam()
print(eggs)