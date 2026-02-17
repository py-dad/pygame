class Switch:
    def __init__(self, numports, poe, iosv):
        self.numports = "Number of Ports: " + str(numports)
        self.poe = "POE supported: " + str(poe)
        self.iosv = "IOS version: " + iosv

    
    def specs(self):
        return '{} {} {}'.format(self.numports, self.poe, self.iosv)
    
    
class Math:
    def __init__(self, num1, num2):
          self.num1 = num1
          self.num2 = num2

    def div(self):
        total = self.num1 * self.num2
        return total
print("Enter first number: ")   
num1 = int(input())

print("Enter second number: ")
num2 = int(input())
values = Math(num1, num2)



print(str(num1) + " times " + str(num2) + " equals " + str(values.div()))


#you can add the variable names for clarity, or simply pass their values
c9300 = Switch(numports= 48, poe = False, iosv = "17.9.7")

print(c9300.specs())

  
