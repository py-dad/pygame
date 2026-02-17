
# calling functions within functions aka call stack
# a() calls b(), b() calls c(), c() calls nothing
# a() then calls d(), d() calls nothing, returns back to a() to print last line
# function calls return to the line number they were called from
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')


def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()