from repositories.order_repo import Order_repository
from services.client_services import Client_ser
from services.employee_services import Employee_services
from services.car_services import Car_services
from services.payment_service import Payment_ser
from models.insurance_model import Insurance
import datetime
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
        date1 = datetime.datetime(int(year1),int(month1),int(day1))
        date1 = date1.date()
        date2 = datetime.datetime(int(year2),int(month2),int(day2))
        date2 = date2.date()
        duration = date2 - date1
        days_num = duration.days
        
        return date1, date2, duration, days_num

    def date_isvalid(self, date_start, date_end, days_num):
        valid_date = True
        error_message = ""
        today_date = datetime.datetime.now()
        # First check if input dates are valid
        if date_start < today_date.date():
            error_message = "Starting date is invalid. (Below today's date)"
            valid_date = False

        if days_num < 1:
            error_message = "Return date is invalid. (Below starting date)."
            valid_date = False

        return valid_date, error_message

    def check_conflict(self, date_start, date_end, car_plate): # check if dates conflict with other orders
        get_order_list = self.order_repo.get_all_orders()
        no_conflict = True
        for line in get_order_list:
            # CR147,2019-06-21,2019-06-28,WS608,Xefu,123456789,Gunnar,228000
            print(line)
            _, start, end, plate, _, _, _, _ = line.split(',')
            order_start = datetime.datetime.strptime(start, '%Y-%m-%d')
            order_end = datetime.datetime.strptime(end, '%Y-%m-%d')
            # CR147,2019-06-21,2019-06-28,WS608,Xefu,123456789,Gunnar,228000
            if car_plate == plate:
                while date_start != date_end:
                    current_date = order_start 
                    while current_date != order_end:
                        print(current_date)
                        if current_date.date() == date_start:
                            print("Conflict!")
                            no_conflict = False
                        current_date += datetime.timedelta(days = 1)
                    date_start += datetime.timedelta(days = 1)
        
        return no_conflict

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

    def get_total_ins_cost(self):
        return self.total_insurance
