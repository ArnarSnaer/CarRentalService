from services.order_services import Order_service

class Service_UI(object):
    def __init__(self):
        self.order_ser = Order_service()
    

    def service_menu(self):
        choice = ""
        while choice != "q":
            print("Current section\n1. Create new order\n2.Delete order\n3.get all orders\nq. Quit")
            choice = input("What would you like to do? ").lower()

            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "q":
                pass
            else:
                print("Please enter a valid operation")
