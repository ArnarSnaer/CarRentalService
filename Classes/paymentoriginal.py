from client import Client
from insurance import Insurance

class Payment(object):
    def __init__(self,base_price,client):
        self.price = 0
        self.base_price = base_price
        self.client = client
        self.total_price = self.base_price + self.price
        self.insurances = []

    def calc_rental_cost(self):
        total_price = self.price + self.base_price
        return total_price
    
    def add_insurance(self,other):
        choice = other
        if choice not in self.insurances:
            print("Insurances: ", self.insurances)
            self.insurances.append(choice)
            self.price = int(self.price + Insurance(choice))
            return self.price
        return "This insurance is already applied to your order"
    
    def get_base_price(self):
        return self.base_price
    
    def get_full_price(self):
        return self.total_price
    
    def __str__(self):
        return "Payment: {}\nClient: {}".format(str(self.total_price),self.client.get_name())
    

person = Client("Jón", "Geysir 7", 5885522,"17 Júní", "1234 5678", "USA", "779")
money = Payment(100000,person)
print(money)
money.add_insurance("t3")
print(money)
money.add_insurance("t1")
money.add_insurance("t1")

cost = money.calc_rental_cost()
print(cost)