# The loops in Language python

name_list = ["geordy", "diamand", "thales"]
for name in name_list:
    print(name)

print()   

for i in range(6): # range(5) ou range(0, 5) = {O, 1, 2, 3, 4} range(n) = [o, n - 1] 
    print(i)

print()

students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)):
    print(i , students[i])