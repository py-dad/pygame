

def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2
    
    elif number % 2 == 1:
       result = 3 * number + 1
       print(result)
       return result


try:
    n = int(input("enter a number: "))
    print("user entered " + str(n))

    while n != 1:
        n = collatz(n)
        print('n = '+ str(n))

except ValueError:
    print("Error! You must enter a valid integer.")