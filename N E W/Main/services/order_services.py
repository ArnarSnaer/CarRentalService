from repositories.order_repo import Order_repository
from services.client_services import Client_ser
from services.employee_services import Employee_services
from services.car_services import Car_services
from services.payment_service import Payment_ser
from models.insurance_model import Insurance
from datetime import datetime
import random
import string

class Order_service(object):
    def __init__(self):
        self.order_repo = Order_repository()
        self.car_serv = Car_services()
        self.insurance = Insurance
        self.car_repo = self.car_serv.car_repo
        self.order_model = self.order_repo.order_model
        self.order_model.zip = self.generate_order_id()
        self.Order_constructor = self.order_repo.order_model
        self.total_insurance = self.order_model().get_total_ins_cost()
        self.total_cost = self.order_model().total_cost

    def add_insurance(self,ins_type):
        added_cost = self.insurance(ins_type)
        self.total_cost = self.total_cost + added_cost
        self.total_insurance += added_cost
        return self.total_cost
    
    def get_status(self):
        plate = self.order_model().get_plate()
        car_info = self.car_repo.find_car(plate)
        car = self.car_serv.create_car(car_info)
        return car.get_status()
    
    def generate_order_id(self):
        id_list = self.order_repo.check_order_id()
        letters = string.ascii_uppercase
        letters_list = list(letters)
        go_again = True
        while go_again:
            id = ""
            for _ in range(2):
                num = random.randint(0,25)
                id += letters_list[num]
            for _ in range(3):
                num_2 = random.randint(0,8)
                id += str(num_2)
            if id not in id_list:
                go_again = False
        return id

    def create_order(self,info_list):
        new_order = self.Order_constructor(info_list[0],info_list[1],info_list[2],info_list[3],info_list[4],info_list[5],info_list[6],info_list[7])
        return new_order

    def find_duration(self, date_start, date_end):
        #Þetta reiknar heildarkostnað (total_price) út frá tímanum sem er gefinn
        day1,month1,year1 = date_start.split(" ")
        day2,month2,year2 = date_end.split(" ")
        date1 = datetime(int(year1),int(month1),int(day1))
        date1 = date1.date()
        date2 = datetime(int(year2),int(month2),int(day2))
        date2 = date2.date()
        duration = date2 - date1
        days_num = duration.days
        
        return date1, date2, duration, days_num
       
# self.order_id,self.date_start,self.date_end,self.plate,self.client_name,self.licence_number,self.employee_name,self.total_cost
    
    def add_order(self,order):
        return self.order_repo.add_order(order)
    
    def remove_order(self,order):
        return self.order_repo.remove_order(order)
    
    def find_order(self,keyword):
        return self.order_repo.find_order(keyword)

    # UPDATE föll

    def change_client(self,order_object): #Client, starting date, return date, car, employee
        pass #Bryta uppl. um client


    def change_start_date(self,order_object,new_date):
        pass
        
        # order_object.date_start = new_date 
        # return order_object
    
    def change_end_date(self,order_object,new_date):
        order_object.date_end = new_date
        return order_object 

    def change_car(self,order_object):
        pass #Breytir upplýsingum um bíl
    
    def change_employee(self,order_object,new_name):
        order_object.employee.change_name(new_name)
        return order_object

    
        
    
