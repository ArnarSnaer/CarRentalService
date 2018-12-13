from services.order_services import Order_service
from ui.car_ui import Car_UI
from ui.employee_ui import Employee_UI
from ui.client_ui import Client_ui

class Order_UI(object):
    def __init__(self):
        self.order_ser = Order_service()
        self.order_repo = self.order_ser.order_repo
        self.car_ui = Car_UI
        self.client_ui = Client_ui
        self.employee_ui = Employee_UI
        self.car_menu = self.car_ui.order_menu
        self.client_menu = self.client_ui.order_menu
        self.employee_menu = self.employee_ui.order_menu  

    def order_menu(self):
        choice = ""
        while choice != "q":
            print("Current section\n1. Create new order\n2. Delete order\n3. Get all orders\n4. Update order\nq. Quit")
            choice = input("What would you like to do? ").lower()

            if choice == "1":
                print("Please enter the neccesery information for the order: ")
                order_id = self.order_ser.generate_order_id()
                start_date = input("Starting date: ")
                end_date = input("Return date: ")
                chosen_car = self.car_menu(Car_UI())
                client = self.client_menu(Client_ui())
                employee = self.employee_menu(Employee_UI())
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
        print("1. Client\n2. Starting date\n3. Return date\n4. Car\n5. Employee name")
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
            current_car = input("Enter licence plate of currnet car ")
            new_car = input("Enter licence plate of new car ")
            pass #Breytir bíl í pöntun

        elif choice == "5":
            new_name = input("Employee name: ")
            new_order = self.order_ser.change_employee(order_object,new_name)

        else:
            print("Invalid choice")

        self.order_repo.remove_order(self.old_order)
        self.order_repo.add_order(new_order)
    
    def print_order(self,order_object):
        self.order_obj = order_object
        self.order_id = self.order_obj.get_order_id()
        self.employee_name = self.order_obj.get_employee_name()

        self.plate = self.order_obj.get_plate()
        self.car_list = self.car_repo.find_car(self.plate)
        self.car = self.car_list[0]
        self.car_type = self.car[0]
        self.car_brand = self.car[1]

        self.client_name = self.order_obj.get_client_name()
        self.licence_num = self.order_obj.get_license_number()
        self.date_start = self.order_obj.get_date_start()
        self.date_end = self.order_obj.get_date_end()

        self.base_insurance = self.order_obj.get_base_insurance()
        self.insurance_price = self.order_obj.get_insurance_price()
        self.insurance_list = self.order_obj.order_payment.insurance_list
        self.total_cost = self.order_obj.get_total_cost()


        print("Order id: {}\nEmployee: {}\n\nStarting date: {}\nReturn date: {}\n".format(self.order_id,self.employee_name,self.date_start,self.date_end))
        print("Car brand: {}\nCar type: {}\nCar plate: {}\n\nClient: {}\nDriver licence number: {}".format(self.car_brand,self.car_type,self.plate,self.client_name,self.licence_num))
        if len(self.insurance_list) != 0:
            print("Insurances")
            for line in self.insurance_list:
                print(line)
        print("Base insurance: {}\nAdditional insurance cost: {}\nTotal price: {}\n".format(self.base_insurance,self.insurance_price,self.total_cost))
    

    def add_insurances_menu(self,order):
        self.order_cost = order
        self.price_list = self.order_cost.get_insurance_price_list() 
        self.title_list = self.order_cost.get_insurance_title_list()

        choice = ""
        while choice != "y" or choice != "n":
            choice = input("> Would you like additional insurances (y/n): ").lower()
            if choice == "y":
                print("Available insurances:")
                for index_num in range(len(self.price_list)):
                #for index_num in range(len(self.price_list)):
                    print("{}. {}: {}isk".format(index_num+1, self.title_list[index_num], self.price_list[index_num]))
                chosen_ins = input("> Choose an insurance to add, you can choose multiple insurances separated by a space:\n")
                chosen_ins_list = chosen_ins.split(" ")
                for ins in chosen_ins_list:
                    ins_int = int(ins)
                    insurance_code = "t" + str(ins_int-1)

                try:
                    self.order_ser.add_insurance(insurance_code)
                except ValueError:
                    print("Chosen insurance does not exist.")


            elif choice == "n":
                pass
            else:
                print("Invalid input. Please try again.")