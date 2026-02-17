##tuple values surrounded by () - immutable
# tuples are faster than lists, but cannot be changed
monday_temperatures = (1,4,5)

print(monday_temperatures)

#list values surrounded by [] - mutable
monday_temperatures2 = [1,4,5]

monday_temperatures2.append(6)

print(monday_temperatures2)

subnets = ["10.101.5.0/24", "10.107.7.0/24"]

print(subnets)

new_sub = input("Enter a new subnet: ")
# Append method called on the subnets list
subnets.append(new_sub)

print(subnets)

#you can assign tuples to tuples, lists, or dictionaries 
interfaces = {"Gi0/1": ("access", "connected to PC", "up"), "Gi0/2": ("trunk", "connected to server", "down")}
print(interfaces)

#extract dict keys
print(interfaces.keys())

print(interfaces.values())