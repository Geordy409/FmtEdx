# create un objet point
'''
class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = point(1,2)
print(f"the coordonate of p1 sont {p1.x} et {p1.y}")
'''
####################################################

# define the class company's plane

'''

class company():
    def __init__(self, name, plane):
        self.name = name
        self.plane = plane

plane1 = company( "AirFrance", "AF017" )
name_client = input("Name :")
print(f" the client's name is {name_client}")
print(f" {name_client} chose the company {plane1.name} and the plane {plane1.plane}")
        
print(f" Good travel {name_client}")

'''

######################################################

# create class flight 

class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if self.open_seats() == 0:
            print("No more seats")
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["Geordy", "Herzy", "Astaire", "Papus"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"{person} added to the flight")
    else:
        print(f"{person} can't be added to the flight")