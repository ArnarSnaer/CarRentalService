from models.order_model import Order

class Order_repository(object):
    def __init__(self):
        self.order_model = Order
        self.ORDER_ID = 0
        self.DATE_START = 1
        self.DATE_END = 2
        self.PLATE = 3
        self.CLIENT_NAME = 4
        self.LICENSE_NUM = 5
        self.EMPLOYEE_NAME = 6
        self.TOTAL_COST = 7

        self.NAME = 0
        self.ADDRESS = 1
        self.PHONE = 2
        self.BIRTHDAY = 3
        self.LICENSE_NUMBER = 4
        self.COUNTRY = 5
        self.THE_ZIP = 6

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
            if line == "\n":
                new_file.write("")
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
        return list_of_orders
    
    def check_order_id(self):
        open_file = open("./data/order.txt","r")
        id_list = []
        for line in open_file:
            info_list = line.split(",")
            id_list.append(info_list[0])
        return id_list


    def update_order(self, old_order, new_element, position):
        '''virkar, indexin eru vitlaus, og vantar að eyða skjalinu áður en ég bæti því inn'''
        order_updated = self.change_element(old_order, new_element, position)
        open_file = open("./data/order.txt", "a+")
        order_updated_instance = Order(order_updated[self.ORDER_ID], order_updated[self.DATE_START], order_updated[self.DATE_END], order_updated[self.PLATE], 
                                order_updated[self.CLIENT_NAME], order_updated[self.LICENSE_NUM],order_updated[self.EMPLOYEE_NAME], order_updated[self.TOTAL_COST])
        self.remove_order(old_order[self.ORDER_ID])
        self.add_order(order_updated_instance)
        open_file.close()
        return order_updated


    def change_element(self, old_order, new_element, position):
        '''searches in a list and changes a selected value and returns the list'''
        
        old_order[position] = new_element
        order_updated = old_order
        return order_updated