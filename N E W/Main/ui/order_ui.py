from services.order_services import Order_service
from ui.car_ui import Car_UI
from ui.employee_ui import Employee_UI
from ui.client_ui import Client_ui

class Order_UI(object):
    def __init__(self):
        self.order_ser = Order_service()
        self.order_repo = self.order_ser.order_repo
        self.car_ui = Car_UI
        self.car_repo = self.car_ui().car_repo
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
                start_date = input("Starting date (DD MM YYYY): ")
                end_date = input("Return date (DD MM YYYY): ")
                try:
                    date1, date2, _, days_num = self.order_ser.find_duration(start_date, end_date)
                except Exception:
                    print("Incorrect date input! Cancelling order and going back to main menu...")
                    break
                check_validity, explanation = self.order_ser.date_isvalid(date1, date2, days_num)
                if check_validity == True:
                    chosen_car = self.car_menu(Car_UI())
                    plate = chosen_car.get_plate()
                    base_price = str(chosen_car.get_price()).strip()
                    order_conflict = self.order_ser.check_conflict(date1, date2, plate)
                    if order_conflict == True:
                        client = self.client_menu(Client_ui())
                        name = client.name
                        lic_num = client.license_num
                        employee = self.employee_menu(Employee_UI())
                        employee_name = employee.get_name()
                        price_duration = self.order_ser.find_base_price_with_duration(int(base_price), days_num)
                        insurance_price, insurance_list = self.order_ser.add_insurance_to_price()
                        final_price = price_duration + insurance_price
                        print("This still work?")
                        info_list = [order_id,date1,date2,plate,name,lic_num,employee_name, int(final_price), days_num]
                        print(info_list)
                        new_order = self.order_ser.create_order(info_list)
                        self.order_ser.add_order(new_order)
                        self.print_order(new_order,base_price,insurance_price,final_price,insurance_list)
                        self.order_ser.change_car_status(plate)
                        print("Order successfully registered into the database")
                    else:
                        print("This car is already reserved during the dates input. Please find another car.")
                        print("")
                else:
                    print(explanation)
                    print("")

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
    
    def print_order(self,order_object, base_price, insurance_price, total_price, insurance_list):
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

        self.base_insurance = "12000"
        self.insurance_price = insurance_price
        self.insurance_list = insurance_list
        self.total_cost = total_price

        print("-"*86)
        print("RECEIPT:")
        print("Order id: {}\nEmployee: {}\n\nStarting date: {}\nReturn date: {}\n".format(self.order_id,self.employee_name,self.date_start,self.date_end))
        print("Car brand: {}\nCar type: {}\nCar plate: {}\n\nClient: {}\nDriver licence number: {}\n".format(self.car_brand,self.car_type,self.plate,self.client_name,self.licence_num))
        if insurance_list == "":
            print("No additional insurances")
        else:
            print("Chosen insurances: {}".format(insurance_list))
        print("Base insurance: {}\nBase car price: {}\nAdditional insurance cost: {}\n\nTotal price: {}\n".format(self.base_insurance,base_price,self.insurance_price,self.total_cost))
        print("-"*86)
