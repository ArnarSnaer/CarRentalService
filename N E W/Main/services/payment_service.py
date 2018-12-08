from models.payment import Payment
from models.insurance import Insurance
from models.creditcard import Creditcard

#EKKI TILBÚIÐ

class Payment_ser(object):
    def __init__(self):
        self.client = Creditcard.client
        self. = Creditcard.
        self.payment = Payment()
        self.insurance = Insurance()
        self.price = self.insurance.price

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