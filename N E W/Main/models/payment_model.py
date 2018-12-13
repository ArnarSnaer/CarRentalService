from models.insurance_model import Insurance

#EKKI TILBÚIÐ

class Payment(object):
    def __init__(self,client_name="",car_price=0,duration=1):
        self.price = car_price
        self.insurances = Insurance()
        self.client_name = client_name
        self.insurance_list = []
        self.total_ins_cost = 0
        self.duration = int(duration)
        self.base_insurance = Insurance("base").get_price()
        self.total_price = self.get_price_with_base()
        self.base_price = self.duration * self.price
    
    def get_base_price(self):
        return self.base_price

    def get_price_with_base(self):
        self.total_price = 0
        self.total_price = self.price * self.duration +  self.base_insurance
        return self.total_price
    
    def get_insurance_title_list(self):
        return self.insurances.get_title_list()

    def get_insurance_cost_list(self):
        return self.insurances.get_price_list()
        
    def get_total_ins_cost(self):
        return self.total_ins_cost

    def __radd__(self,other):
        return int(self.price + other)    

    def __str__(self):
        return "{}".format(str(self.total_price))
    