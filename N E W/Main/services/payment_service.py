from models.payment_model import Payment

#EKKI TILBÚIÐ

class Payment_ser(object):
    def __init__(self):
        self.payment = Payment()
        self.client = self.payment.client
        self.credit = self.payment.credit
        self.insurances = self.payment.insurances
        self.price = self.insurances.price

    def add_insurance(self,other):
        choice = other
        if choice not in self.payment.insurance_list:
            self.payment.insurance_list.append(choice)
            print("Insurances: ", self.insurances)
            self.price = int(self.price + self.insurances(choice))
            self.payment.total_price += self.price
            return self.price
        else:
            return "This insurance is already applied to your order"