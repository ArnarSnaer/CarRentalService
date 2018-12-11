class Calculator(object):
    def __init__(self, veh_type, duration, price=0):
        self.veh_type = veh_type
        self.duration = duration
        self.price = price
    
    def __str__(self):
        return "{},{},{}".format(self.veh_type, self.duration, self.price)

    def get_veh_type(self):
        return self.veh_type

    def get_duration(self):
        return self.duration

    def get_price(self):
        return self.price
