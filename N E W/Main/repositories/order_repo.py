from models.order_model import Order

class Order_repository(object):
    def __init__(self):
        self.order_model = Order()
        self.order_constructor = Order
        self.order_payment = self.order_model.total_cost
        self.info = self.order_model.info
         

    def add_order(self,order):
        
        open_file = open("./data/order.txt","r")
        
        # self.order_id = self.Order.order_id
        # self.date_start = self.Order.date_start
        # self.date_end = self.Order.date_end
        # self.car = self.Order.car
        # self.driver = self.Order.client.get_name()
        # self.employee = self.Order.employee.get_name()
        # self.licence_plate = self.Order.car.plate
        # self.total_cost = self.Order.total_cost

        open_file.write("{}".format(str(self.order_model)))
        open_file.close()

    def remove_order(self,order_id):
        open_file = open("./data/order.txt","w")
        old_file = open_file.readlines()
        open_file.close()

        new_file = open_file("./data/orders.txt","r")
        for line in old_file:
            if order_id not in line:
                new_file.write(line)
        
        new_file.close()
    
    def find_order(self, searchword):
        open_file = open("./data/order.txt","r")
        order_list = []
        for line in open_file:
            if searchword in line:
                found_list = line.split(",")
                order_list.append(found_list)
        return order_list
    
    def get_all_orders(self):
        open_file = open("./data/order.txt","r")
        list_of_orders = open_file.readlines()
        all_cars = ""
        open_file.close()
        for line in list_of_orders:
            all_cars += line
            if line != list_of_orders[-1]:
                all_cars += "\n"
        return all_cars

    def update_order(self):
        print("What would you like to update? (Please input integer choice)")
        print("1. Client\n2. Starting date\n3. Retrun date\n4. Car\n5. Employee name")
        
        choice = int(input(""))
        change = input("New info is: ")
        
        self.info[choice-1] = change
        return self.info
    
    def check_order_id(self):
        open_file = open("./data/order.txt","r")
        id_list = []
        for line in open_file:
            info_list = line.split(",")
            id_list.append(info_list[0])
        return id_list