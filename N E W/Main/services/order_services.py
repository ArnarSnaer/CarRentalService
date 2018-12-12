from repositories.order_repo import Order_repository
from services.client_services import Client_ser
from services.employee_services import Employee_services
from services.car_services import Car_services
#from models.order_model import Order
import random
import string

class Order_service(object):
    def __init__(self):
        self.order_repo = Order_repository()
        self.order_model = self.order_repo.order_model
        self.order_model.zip = self.generate_order_id()
        self.Order_constructor = self.order_repo.order_constructor

    def add_insurance(self,ins_type):
        self.order_model.price.add_insurance(ins_type)
        return self.order_model.price
    
    def get_status(self):
        status = self.order_model.get_status()
        return status
    
    def generate_order_id(self):
        id_list = self.order_repo.check_order_id()
        letters = string.ascii_uppercase.split()
        go_again = True
        while go_again:
            id = ""
            for _ in range(2):
                num = random.randint(0,26)
                id += letters[num]
            for _ in range(3):
                num_2 = random.randint(0,9)
                id += str(num_2)
            if id not in id_list:
                go_again = False
        return id

    def create_order(self,info_list):
        new_order = self.Order_constructor(info_list[0],info_list[1],info_list[2],info_list[3],info_list[4],info_list[5])
        return new_order
    
    def add_order(self,order):
        return self.order_repo.add_order(order)
    
    def remove_order(self,order):
        return self.order_repo.remove_order(order)
    
    def find_order(self,keyword):
        return self.order_repo.find_order(keyword)

    # UPDATE föll

    def change_start_date(self,order_object,new_date):
        order_object.date_start = new_date 
        return order_object
    
    def change_end_date(self,order_object,new_date):
        order_object.date_end = new_date
        return order_object 

    def change_employee(self,order_object,new_name):
        order_object.employee.change_name(new_name)
        return order_object

    def change_client(self,order_object): #Client, starting date, return date, car, employee
        pass #Bryta uppl. um client
        
    def change_car(self,order_object):
        pass #Breytir upplýsingum um bíl