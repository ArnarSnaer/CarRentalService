from models.client_model import Client
from models.insurance_model import Insurance
from models.car_model import Car
from models.creditcard_model import Creditcard

#EKKI TILBÚIÐ

class Payment(object):
    def __init__(self,client,car_price,duration=1):
        self.price = car_price
        self.credit = Creditcard
        self.insurances = Insurance
        self.client = client
        self.car = car
        self.insurance_list = []
        self.base_insurance = Insurance("base")
        self.total_price = (self.price * duration) +  self.base_insurance
    
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