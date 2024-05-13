# create a function calcul a square and print by decreasing order or descending order 

def carre_function(x):
    return x*x

for i in range (10):
        if carre_function(i + 1) > carre_function(i):
            print(carre_function(i + 1))
        else:
             print(carre_function(i))


