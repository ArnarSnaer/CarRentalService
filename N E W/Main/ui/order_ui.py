from services.order_services import Order_service
from ui.car_ui import Car_UI
from ui.employee_ui import Employee_UI
from ui.client_ui import Client_ui

class Order_UI(object):
    def __init__(self):
        self.order_ser = Order_service()
        self.car_ui = Car_UI
        self.client_ui = Client_ui
        self.employee_ui = Employee_UI

        self.car_menu = self.car_ui.order_menu
        self.client_menu = self.client_ui.order_menu
        self.employee_menu = self.employee_ui.order_menu    

    def service_menu(self):
        choice = ""
        while choice != "q":
            print("Current section\n1. Create new order\n2.Delete order\n3.get all orders\n4. Update order\nq. Quit")
            choice = input("What would you like to do? ").lower()

            if choice == "1":
                print("Please enter the neccesery information for the order: ")
                order_id = self.order_ser.generate_order_id()
                start_date = ("Starting date: ")
                end_date = ("Return date: ")
                chosen_car = self.car_menu
                client = self.client_menu
                employee = self.employee_menu
                info_list = [order_id,start_date,end_date,chosen_car,client,employee]
                new_order = self.order_ser.create_order(info_list)
                self.order_ser.add_order(new_order)

            elif choice == "2":
                keyword = input("Enter the order id of the order you want to delete:\n")
                order_list = self.order_ser.find_order(keyword)
                found_order = order_list[0]
                self.order_ser.remove_order(found_order)
                print("Order removed.\n")

            elif choice == "3":
                print(self.order_ser.order_repo.get_all_orders())
            else:
                print("Please enter a valid operation")
