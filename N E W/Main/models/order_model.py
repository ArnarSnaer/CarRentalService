from models.client_model import Client
from models.car_model import Car
from models.employee import Employee 

class Order(object):
    def __init__(self,order_id="AA111", date_start="1 1 2000", date_end="2 1 2000",plate = "",client_name = "",licence_number = "",employee_name = "",total_cost=0, duration=1):
        self.order_id = order_id
        self.date_start = date_start
        self.date_end = date_end
        self.plate = plate
        self.client_name = client_name
        self.employee_name = employee_name
        self.licence_number = licence_number
        self.total_cost = total_cost
        self.duration = duration
        self.info = [self.order_id,self.date_start,self.date_end,self.plate,self.client_name,self.licence_number,self.employee_name]

    def __str__(self):
        return "{},{},{},{},{},{},{},{}".format(self.order_id,self.date_start,self.date_end,self.plate,self.client_name,self.licence_number,self.employee_name,self.total_cost)

    def get_order_id(self):
        return self.order_id

    def get_date_start(self):
        return self.date_start

    def get_date_end(self):
        return self.date_end

    def get_plate(self):
        return self.plate

    def get_client_name(self):
        return self.client_name

    def get_license_number(self):
        return self.licence_number

    def get_employee_name(self):
        return self.employee_name

    def get_total_cost(self):
        return self.total_cost
