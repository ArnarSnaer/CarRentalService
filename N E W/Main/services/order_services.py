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
        self.total_cost = self.order_model().total_cost
        self.payment_ser = Payment_ser()

        # self.order_model = Order

        self.ORDER_ID = 0
        self.DATE_START = 1
        self.DATE_END = 2
        self.PLATE = 3
        self.CLIENT_NAME = 4
        self.Order_LICENSE_NUM = 5
        self.EMPLOYEE_NAME = 6
        self.TOTAL_COST = 7

        self.NAME = 0
        self.ADDRESS = 1
        self.PHONE = 2
        self.BIRTHDAY = 3
        self.LICENSE_NUM = 4
        self.COUNTRY = 5
        self.THE_ZIP = 6
    
        # added_cost = self.insurance(ins_type)
        # print("AAAAAAAA: ", added_cost)
        # self.total_cost = self.total_cost + added_cost
        # self.total_insurance += added_cost
        # return self.total_cost
    
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
        try:
            new_order = self.Order_constructor(info_list[0],info_list[1],info_list[2],info_list[3],info_list[4],info_list[5],info_list[6],info_list[7], info_list[8])
        except Exception:
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
            _, start, end, plate, _, _, _, _ = line.split(',')
            order_start = datetime.datetime.strptime(start, '%Y-%m-%d')
            order_end = datetime.datetime.strptime(end, '%Y-%m-%d')
            # CR147,2019-06-21,2019-06-28,WS608,Xefu,123456789,Gunnar,228000
            if car_plate == plate:
                while (date_start != date_end):
                    current_date = order_start 
                    while current_date != order_end:
                        if current_date.date() == date_start:
                            no_conflict = False
                        current_date += datetime.timedelta(days = 1)
                    date_start += datetime.timedelta(days = 1)
        if date_start > date_end:
            no_conflict = False
        return no_conflict

    def find_base_price_with_duration(self, base, days):
        total_price = base * days + 12000
        return total_price

    def add_insurance_to_price(self):
        insurance_price = 0
        applied_insurances = []
        chosen_ins = ""
        choice = ""
        while True:
            print("Current chosen insurances: {}".format(applied_insurances)) #Þarf að færa þetta á ui
            print("Add insurances to car, or type 'q' to continue\n1. Water Damage insurance: 10'000 ISK\n2. CASCO insurance: 20'000 ISK\n3. Theft insurance: 5'000 ISK\n4. Collision damage insurance")
            choice = input("> Enter choice here: ")
            if choice == ("1" or "Water Damage Insurance"):
                    if "1" in applied_insurances:
                            print("Already registered")
                    else:
                            insurance_price += 10000
                            applied_insurances.append("1")
                            chosen_ins += "Water Damage Insurance,"
            if choice == ("2" or "CASCO insurance"):
                    if "2" in applied_insurances:
                            print("Already registered")
                    else:
                            insurance_price += 20000
                            applied_insurances.append("2")
                            chosen_ins += "CASCO insurance,"
            if choice == ("3" or "Some other insurance"):
                    if "3" in applied_insurances:
                            print("Already registered")
                    else:
                            insurance_price += 5000
                            applied_insurances.append("3")
                            chosen_ins += "Theft insurance,"
            if choice == ("4" or "Collision damage insurance"):
                    if "4" in applied_insurances:
                            print("Already registered")
                    else:
                            insurance_price += 15000
                            applied_insurances.append("4")
                            chosen_ins += "Collision damage insurance,"
            if choice == ("q" or "Q"):
                    break
            else:
                    print("Invalid input/insurance already chosen")

        return insurance_price, chosen_ins[:-1]

    def change_car_status(self, plate):
        result = self.car_repo.find_car(plate)
        real_list = result[0]
        pos = real_list[4]
        if pos == "True":
            status = "False"
        elif pos == "False":
            status = "True"
        real_list[4] = status
        changed_car_status = self.car_serv.create_car(real_list)
        self.car_repo.remove_car(plate)
        self.car_repo.add_car(changed_car_status)

# 12000,10000,20000,5000
# self.order_id,self.date_start,self.date_end,self.plate,self.client_name,self.licence_number,self.employee_name,self.total_cost
    
    def add_order(self,order):
        return self.order_repo.add_order(order)
    
    def remove_order(self,order):
        return self.order_repo.remove_order(order)
    
    def find_order(self,keyword):
        return self.order_repo.find_order(keyword)

    # UPDATE föll

    def change_client(self, client_info_list, old_order):
        new_name = client_info_list[self.NAME]
        new_license_num = client_info_list[self.LICENSE_NUM]
        name_position = self.CLIENT_NAME
        license_position = self.Order_LICENSE_NUM
        name_updated = self.order_repo.update_order(old_order, new_name, name_position)
        license_and_name_updated = self.order_repo.update_order(name_updated, new_license_num, license_position)
        
        return license_and_name_updated
        

    def change_date(self, new_date, old_order, is_start):
        date_updated =''
        ''' is_start tells us if we are working with the start date or the end date'''
        if is_start:
            start_date = new_date
            end_date = old_order[self.DATE_END]
            end_date = end_date.split("-")
            end_date = ''.join([end_date[2]," ", end_date[1]," ", end_date[0]])
            date_position = self.DATE_START
        else:
            end_date = new_date
            start_date = old_order[self.DATE_START]
            start_date = start_date.split("-")
            start_date = ''.join([start_date[2]," ", start_date[1]," ", start_date[0]])  
            date_position = self.DATE_END  
        
        car_plate = old_order[self.PLATE]
        date1, date2, duration, days_num = self.find_duration(start_date, end_date)
        valid_date, error_message = self.date_isvalid(date1, date2,days_num)
        if valid_date:
            no_conflict=  self.check_conflict(date1, date2, car_plate)
            if no_conflict:
                if is_start:
                    date_updated = self.order_repo.update_order(old_order, date1, date_position)
                else:
                    date_updated = self.order_repo.update_order(old_order, date2, date_position)
            else:
                print(no_conflict)
                date_updated = None
        else:
            date_updated = None
        return date_updated
    
    def change_car(self,order_object):
        pass #Breytir upplýsingum um bíl
    
    def change_employee(self,order_object,new_name):
        order_object.employee.change_name(new_name)
        return order_object

    def check_date_format(self, a_string):
        try:
            for element in a_string:
                if element != " ":
                    int(element)
            return True
        except ValueError:
            return None
            