
#corey schaefer tutorial on classes

class Employee:
    #instance is the first agrument automatically, typically called self
    #self stands in for the employee object, ex emp_1, emp_2, etc
    def __init__(self, first, last, pay):
        #name, email, and pay are all attributes of our class
        #these variable names could be same or different than arugment name
        self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    #create a method called full name
    def fullname(self):
        #use self so that it will work with all instances. '{}, {}' are placeholders
        return '{} {}'.format(self.fname, self.last)

#class is blueprint for creating instances
#each employee is instance of class


emp_1 = Employee('Ken', 'Jennings', 50000)
emp_2 = Employee('Alice', 'Darnell', 60000)

#call the fullname function on emp_1, and print result
#note nothing needs to be passed to function
print(emp_1.fullname())

#you can also run these methods using the class name itself
#if you run method from the Class directly, you have to pass in the instance 
print(Employee.fullname(emp_2))

#print(emp_1)
#print(emp_2)

#print(emp_1.email)

#alternatively you "could "manually create instance variable - not ideal when you have several instances 

#emp_1.first = 'Ken'
#emp_1.last = 'Jennings'
#emp_1.email = 'ken.jennings@jptv.com'
#emp_1.pay = 50000

#print(emp_1.email)

