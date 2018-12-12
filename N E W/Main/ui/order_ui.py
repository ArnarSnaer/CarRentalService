from services.order_services import Order_service
from ui.car_ui import Car_UI
from ui.employee_ui import Employee_UI
from ui.client_ui import Client_ui

class Order_UI(object):
    def __init__(self):
        self.order_ser = Order_service()
        self.order_repo = self.order_ser.order_repo
        self.car_ui = Car_UI()
        self.client_ui = Client_ui()
        self.employee_ui = Employee_UI()

        self.car_menu = self.car_ui.order_menu
        self.client_menu = self.client_ui.order_menu
        self.employee_menu = self.employee_ui.order_menu 

    def order_menu(self):
        choice = ""
        while choice != "q":
            print("Current section\n1. Create new order\n2.Delete order\n3.get all orders\n4. Update order\nq. Quit")
            choice = input("What would you like to do? ").lower()

            if choice == "1":
                print("Please enter the neccesery information for the order: ")
                order_id = self.order_ser.generate_order_id()
                start_date = ("Starting date: ")
                end_date = ("Return date: ")
                chosen_car = self.car_menu()
                client = self.client_menu()
                employee = self.employee_menu()
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
            
            elif choice == "4":
                order_id = input("Input id of order you want to change (AAA11): ")
                found_order = self.order_repo.find_order(order_id)
                self.change_order(found_order)
            else:
                print("Please enter a valid operation")

    def change_order(self,order_object):
        print("1. Client\n2. Starting date\n3. Retrun date\n4. Car\n5. Employee name")
        choice = input("What would you like to update? (Please input integer choice): ")
        self.old_order = order_object

        if choice == "1":
            pass #Bryta uppl. um client

        elif choice == "2":
            new_date = input("New starting date (DD/MM/YYYY):\n ")
            new_order = self.order_ser.change_start_date(order_object,new_date)

        elif choice == "3":
            new_date = input("New return date (DD/MM/YYYY):\n ")
            new_order = self.order_ser.change_end_date(order_object,new_date)

        elif choice == "4":
            pass #Breytir upplýsingum um bíl

        elif choice == "5":
            new_name = input("Employee name: ")
            new_order = self.order_ser.change_employee(order_object,new_name)

        else:
            print("Invalid choice")

        self.order_repo.remove_order(self.old_order)
        self.order_repo.add_order(new_order)