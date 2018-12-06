from client import Client
from insurance import Insurance
from car import Car

class Payment(object):
    def __init__(self,client,car,duration=1):
        self.price = 0
        self.base_price = car.get_price()
        self.client = client
        self.insurances = []
        self.base_insurance = Insurance("base")
        self.total_price = (car.price * duration) +  self.base_insurance
        self.car = car
    
    def add_insurance(self,other):
        choice = other
        if choice not in self.insurances:
            self.insurances.append(choice)
            print("Insurances: ", self.insurances)
            self.price = int(self.price + Insurance(choice))
            self.total_price += self.price
            return self.price
        else:
            return "This insurance is already applied to your order"
    
    def get_full_price(self):
        return self.total_price
    
    def __str__(self):
        return "Payment: {}\nClient: {}".format(str(self.total_price),self.client.get_name())
    
'''
person = Client("Jón", "Geysir 7", 5885522,"17 Júní", "1234 5678", "USA", "779")
car = Car("Jeppi","Toyota Land Cruiser","ER C01","4x4",True,False,60000,"diesel",14000)
money = Payment(person,car)
print(money)
print("")
money.add_insurance("t3")
print(money)
#money.add_insurance("t1")
#print(money)
#money.add_insurance("t1")
#cost = money.calc_rental_cost()
#print(cost)
'''