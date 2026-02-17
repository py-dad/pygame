def foo(list1):
    for i in list1:
        if i in list1 != int:
            list1.remove(i)
    print(list1)
       

def fooSimpler(list1):
    return [i for i in list1 if isinstance(i, int)]


fooSimpler([99, 'no data', 101, 'data no', 103, 'data dude', 77, 'data mom', 33, 'data base'])