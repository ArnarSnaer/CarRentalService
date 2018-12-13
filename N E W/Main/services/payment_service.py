from models.payment_model import Payment
from models.insurance_model import Insurance

#EKKI TILBÚIÐ

class Payment_ser(object):
    def __init__(self):
        self.payment = Payment()
        self.insurance = Insurance
        self.client_name = self.payment.client_name
        self.price = self.insurance().get_price()

    def add_insurance(self,other):
        choice = other
        if choice not in self.payment.insurance_list:
            self.payment.insurance_list.append(choice)
            print("Insurances: ", self.insurance)
            self.price = int(self.price + self.insurance(choice)) #NOT CALLABLE?
            self.payment.total_price += self.price
            self.payment.total_insurance_cost += self.price
            return self.price
        else:
            return "This insurance is already applied to your order"
        
    def get_base_price(self):
        return self.payment.get_base_price()
    