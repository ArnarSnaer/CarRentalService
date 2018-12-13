from models.order_model import Order

class Order_repository(object):
    def __init__(self):
        self.order_model = Order

    def add_order(self,order_model):
        open_file = open("./data/order.txt","a+")

        order_id = order_model.get_order_id()
        date_start = order_model.get_date_start()
        date_end = order_model.get_date_end()
        plate = order_model.get_plate()
        client_name = order_model.get_client_name()
        license_number = order_model.get_license_number()
        employee_name = order_model.get_employee_name()
        total_cost = order_model.get_total_cost()

        open_file.write("{},{},{},{},{},{},{},{}\n".format(order_id,date_start,date_end,plate,client_name,license_number,employee_name,total_cost))

        open_file.close()

    def remove_order(self,order_id):
        open_file = open("./data/order.txt","r")
        old_file = open_file.readlines()
        open_file.close()

        new_file = open("./data/order.txt","w")
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
                
        print(order_list)
        return order_list
    
    def get_all_orders(self):
        open_file = open("./data/order.txt","r")
        list_of_orders = open_file.readlines()
        return list_of_orders
    
    def check_order_id(self):
        open_file = open("./data/order.txt","r")
        id_list = []
        for line in open_file:
            info_list = line.split(",")
            id_list.append(info_list[0])
        return id_list