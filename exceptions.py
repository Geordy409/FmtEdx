# The exception's notioin in python: the word importants are: 
'''

try, except, and finally

'''

#  define function with exceptibons to handle(gérer)/manage

import sys

def div_zero():
    a = int(input("a:"))
    b = int(input("b: "))

    try:
        result = a / b
        print(f"On calcule la division a par b : {result}")
    except ZeroDivisionError:
        print("Une exception s'est produite lors de la division par zéro")
        sys.exit(1)

div_zero()

try:
    div_zero()
    print("Aucune exception n'a été levée")
except ZeroDivisionError:
    print("Une exception s'est produite")
    sys.exit(1)