# create a decorator: a function taking a in function as enter or in Parameter and add modification 

def announce (f):
    def wrapper():
        print("I'm a functioin without modification")
        f()
        print("Im a new function")
    return wrapper

@announce  # with this keyword f() will become the function hello()
def hello():
    print("Hello")

hello()

'''
les decorateurs( decorators) permettent de faire beaucoup de chose en web
par exmple on peut les utiliser pour modifier les propriétés de fonctions,en ameliorant 
les capacités de fonctions les utilisateurs( voir que les propreties des admins is diff des simples users)
'''
