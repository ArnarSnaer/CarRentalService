from repositories.order_repo import Order_repository
import random
import string

class Order_service(object):
    def __init__(self):
        self.order_repo = Order_repository

    def add_insurance(self,ins_type):
        self.order_repo.price.add_insurance(ins_type)
        return self.order_repo.price
    
    def get_status(self):
        status = self.order_repo.order_model.status
        return status
    
    def generate_order_id(self):
        id_list = self.order_repo.check_order_id()
        letters = string.ascii_uppercase.split()
        go_again = True
        while go_again
            id = ""
            for _ in range(2):
                num = random.randint(0,26)
                id += letters[num]
            for _ in range(3)
                num_2 = random.randint(0,9)
                id += str(num2)
            if id not in id_list:
                go_again = False
        return id

    def create_order(self,info_list):