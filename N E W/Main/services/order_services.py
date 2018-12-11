from repositories.order_repo import Order_repository

class Order_service(object):
    def __init__(self):
        self.order_repo = Order_repository

    def add_insurance(self,ins_type):
        self.order_repo.price.add_insurance(ins_type)
        return self.order_repo.price
    
    