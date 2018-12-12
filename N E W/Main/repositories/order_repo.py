from models.order_model import Order

class Order_repository(object):
    def __init__(self):
        self.order_model = Order
        #self.order_payment = self.order_model().total_cost
        #self.info = self.order_model().info
         

    def add_order(self,order):
        
        open_file = open("./data/order.txt","r")
        open_file.write("{}".format(str(order)))
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
    
    def check_order_id(self):
        open_file = open("./data/order.txt","r")
        id_list = []
        for line in open_file:
            info_list = line.split(",")
            id_list.append(info_list[0])
        return id_list