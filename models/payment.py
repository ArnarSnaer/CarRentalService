from client import Client
from insurance import Insurance
from find_client import Find_client

class Payment(object):
    def __init__(self,price=0,base_price=0,client_name="John"):
        self.price = price
        self.base_price = base_price
        self.client_name = client_name
        self.client_info = Find_client(self.client_name)
        self.client = Client(self.client_info)
        self.total_price = 0
        self.insurances = []
        print(self.client_info)



    def calc_rental_cost(self):
        total_price = self.price + self.base_price
        return total_price
    
    def add_insurance(self,other):
        choice = other
        if choice not in self.insurances:
            self.insurances.append(choice)
            return self.total_price + self.insurances(choice)
        return "This insurance is already applied to your order"
    
    def get_base_price(self):
        return self.base_price
    
    def get_full_price(self):
        return self.total_price
    


money = Payment()
print(money)