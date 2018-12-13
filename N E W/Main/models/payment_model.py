from models.insurance_model import Insurance

#EKKI TILBÚIÐ

class Payment(object):
    def __init__(self,client_name="",car_price=0,duration=1):
        self.price = car_price
        self.insurances = Insurance()
        self.client_name = client_name
        self.insurance_list = []
        self.duration = int(duration)
        self.base_insurance = Insurance("base").get_price()
        self.total_price = self.get_price_with_base()
    
    def get_price_with_base(self):
        self.total_price = 0
        self.total_price = self.price * self.duration +  self.base_insurance
        return self.total_price
    
    def get_insurance_title_list(self):
        return self.insurances.get_title_list()

    def get_insurance_cost_list(self):
        return self.insurances.get_price_list()
    
    def __str__(self):
        return "{}".format(str(self.total_price))
    