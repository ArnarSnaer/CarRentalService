from client import Client
from creditcard import Creditcard
from datetime import datetime
from car import Car
from employee import Employee
from payment import Payment

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

    def get_status(self):
        return self.car.get_status()
        #Þarf að impliment-a þetta öðruvísi
    
    def get_base_price(self): #laga þegar þetta virkar allt
        return self.payment.base_price


    def calc_duration(self):
        day1,month1,year1 = self.date_start.split(" ")
        day2,month2,year2 = self.date_end.split(" ")
        date1 = datetime(int(year1),int(month1),int(day1))
        date2 = datetime(int(year2),int(month2),int(day2))
        duration = date2 - date1
        days_num = duration.days
        return days_num

    def create_payment(self):
        order_payment = Payment(self.client, self.car)
        return order_payment

    def calc_total_cost(self,order_payment,days_num):
        payment_val = order_payment.calc_rental_cost(days_num,self.car)
        self.total_cost = self.price + payment_val
        print("THING: ", self.price, " ", payment_val)
        return self.total_cost
    
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
    
    #def calc_total_cost(self):
     #   payment_val = create_payment() 
      #  self.total_cost = self.price + payment_val
       # return self.total_cost


card = Creditcard("Ari Halldórsson","Gullfoss 2", 5812345, "5849 9471 0372 0813", "10/21", "123")
bill = Car("Jeppi","Toyota Land Cruiser","ER C01","4x4",True,False,60000,"diesel")
bill.check_price()
vinur = Client("Jón Gústafsson", "Geysir 7", 5885522,"17 Júní", "1234 5678", "USA", "779")
gunnar = Employee("Gunnar Stefánsson")


first_order = Order("A1",card,"1 1 2014","1 6 2014",bill,vinur,gunnar)
num_of_days = first_order.calc_duration()
test_payment = first_order.create_payment()
first_order.calc_total_cost(test_payment,num_of_days)
print(first_order)
#def __init__(self,order_id,credit_info, date_start, date_end,car,client,employee):