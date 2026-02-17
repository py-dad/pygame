#lists - values without keys
#student_grades = [9.1, 8.8, 7.5]

#mysum = sum(student_grades)
#length = len(student_grades)
#mean = mysum / length
#print(mean) 

#dictionary - key: value pairs 
#dictionaries more appropriate when a value has a specific identity, ie student and grade
#the functions above won't work on dictionary types, instead you need to pull the values
#to peform the function

student_grades = {"Marry": 9.1, "Sim": 8.8 , "John": 7.5}

mysum = sum(student_grades.values()) #get values from dictionary, then perform math functions 
length = len(student_grades)
mean = mysum / length
print(mean)