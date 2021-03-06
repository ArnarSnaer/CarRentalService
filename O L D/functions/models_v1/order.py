from class_client import Client
from class_creditcard import Creditcard
from datetime import datetime
from class_car import Car
from class_employee import Employee
from class_payment import Payment

class Order(object):
    def __init__(self,order_id,credit_info, date_start, date_end,car,client,employee):
        self.order_id = order_id
        self.credit_info = credit_info
        self.date_start = date_start
        self.date_end = date_end
        self.car = car
        self.client = client
        self.driver = client.get_name()
        self.employee = employee.get_name()
        self.licence_plate = car.plate
        self.price = car.price
        self.total_cost = 0
        self.min_duration = 1
        self.info= [self.credit_info,date_start,date_end,self.car,self.employee]

        #Þetta reiknar heildarkostnað (total_price)
        # 1. Reiknar fjölda daga sem pöntunin stendur yfir
        # 2. Býr til payment og skilartölugildi hennar
        day1,month1,year1 = self.date_start.split(" ")
        day2,month2,year2 = self.date_end.split(" ")
        date1 = datetime(int(year1),int(month1),int(day1))
        date2 = datetime(int(year2),int(month2),int(day2))
        duration = date2 - date1
        days_num = duration.days

        self.order_payment = Payment(self.client,self.car,days_num)
        self.total_cost = self.order_payment
        

    def get_status(self):
        return self.car.get_status()
        #Þarf að impliment-a þetta öðruvísi
    
    def get_base_price(self):
        return self.order_payment.base_price

    def calc_duration(self,date_start,date_end):
        day1,month1,year1 = date_start.split(" ")
        day2,month2,year2 = date_end.split(" ")
        date1 = datetime(int(year1),int(month1),int(day1))
        date2 = datetime(int(year2),int(month2),int(day2))
        duration = date2 - date1
        days = duration.days
        return days
    
    def add_insurance(self,price,other):
        self.price.add_insurance(other)
        return self.price
    
    def update_order(self):
        print("What would you like to update? (Please input integer choice)")
        print("1. Credit information\n2. Starting date\n3. Retrun date\n4. Car\n5. Employee name")
        
        choice = int(input(""))
        change = input("New info is: ")
        
        self.info[choice-1] = change
        return self.info
    
    def __str__(self):
        return "Order id: {}\nClient: {}\nCar: {}\nLicense plate: {}\nStarting Date: {}\nReturn date: {}\nPrice: {}\nEmployee: {}".format(self.order_id,self.client.get_name(),self.car.get_type(),self.car.get_plate(),self.date_start,self.date_end,self.total_cost,self.employee)
    
    def __iter__(self):
        return iter(self.info)
    
    def __getitem__(self,index_num):
        return self.info[index_num]

'''
card = Creditcard("Ari","Gullfoss 2", 5812345, "5555 5555 5555 5555", "10/21", "123")
bill = Car("Jeppi","Toyota Land Cruiser","ER C01","4x4",True,False,60000,"diesel")
vinur = Client("Jón Gústafsson", "Geysir 7", 5885522,"17 Júní", "1234 5678", "USA", "779")
gunnar = Employee("Gunnar")


first_order = Order("AC 101",card,"1 1 2014","1 1 2015",bill,vinur,gunnar)
#first_order.order_payment.add_insurance("t2")
print(first_order)
#def __init__(self,order_id,credit_info, date_start, date_end,car,client,employee):
'''