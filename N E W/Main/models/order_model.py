from models.client_model import Client
from datetime import datetime
from models.car_model import Car
from models.employee import Employee #Endurskýra
from models.payment_model import Payment

class Order(object):
    def __init__(self,order_id, date_start, date_end,car,client,employee):
        self.order_id = order_id
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

        #Þetta reiknar heildarkostnað (total_price) út frá tímanum sem er gefinn
        day1,month1,year1 = self.date_start.split(" ")
        day2,month2,year2 = self.date_end.split(" ")
        date1 = datetime(int(year1),int(month1),int(day1))
        date2 = datetime(int(year2),int(month2),int(day2))
        duration = date2 - date1
        days_num = duration.days

        self.order_payment = Payment(self.client,self.car,days_num)
        self.total_cost = self.order_payment
        
    def get_status(self):
        return self.car.status
        #Þarf að impliment-a þetta öðruvísi
    
    def get_base_price(self):
        return self.order_payment.base_price
    
    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.order_id,self.client.get_name(),self.car.get_plate(),self.date_start,self.date_end,self.total_cost,self.employee)
    


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