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

    def choose_order(self):
        order_list = self.order_repo.get_all_orders()
        print(order_list)
        counter = 1
        for item in order_list:
            try:
                item_list = item.split(",")
                order_object = self.order_ser.create_order(item_list)
                order_id = self.order_repo.order_model.get_order_id(order_object)
                license_num = self.order_repo.order_model.get_plate(order_object)
                client = self.order_repo.order_model.get_client_name(order_object)
                start = self.order_repo.order_model.get_date_start(order_object)
                end = self.order_repo.order_model.get_date_end(order_object)
                price = self.order_repo.order_model.get_total_cost(order_object)
                price = price[:-1]
                print("{:>5d}. {} Order ID: {:>5s}{:>5s}License plate: {:>5s}{:>5s}Client: {:>5s} renting from {:>5s} to {:>5s} for a total of {:>5s}".format(counter,"|",order_id,"", license_num,"",client, start,end, price))
                print("")
                counter += 1
            except Exception:
                pass

        quit = False
        print("Complete! Here are all the results of the search.\n")
        while not quit:
            choice = input("> Enter the number of the order you wish to remove, or write 'q' to quit: ")
            the_choice = self.check_input(choice, 'q')
            if not the_choice:
                print("Please input a valid integer") 
            elif the_choice == 'q':
                quit = True
                print("Order not chosen, aborting") 
                return None
            elif the_choice in range(counter+1):    
                whole_order =  order_list[the_choice-1]
                order_id = whole_order.split(",")
                order_id = order_id[0] 
                return order_id
            else:
                print("Please input a valid integer") 
            
    def order_menu(self):
        choice = ""
        while choice != "q":
            print("Current section: Order\n1. Create new order\n2. Delete order\n3. Get all orders\n4. Update order\nq. Back")
            choice = input("> What would you like to do? ").lower()

            if choice == "1":
                print("Please enter the neccesery information for the order: ")
                order_id = self.order_ser.generate_order_id()
                start_date = input("Starting date (DD MM YYYY): ")
                end_date = input("Return date (DD MM YYYY): ")
                print("\n")
                try:
                    date1, date2, _, days_num = self.order_ser.find_duration(start_date, end_date)
                except Exception:
                    print("Incorrect date input! Cancelling order and going back to main menu...")
                    break
                check_validity, explanation = self.order_ser.date_isvalid(date1, date2, days_num)
                if check_validity == True:
                    try:
                        chosen_car = self.car_menu(Car_UI())
                        if chosen_car == None:
                            choice = "q"
                            break
                        plate = chosen_car.get_plate()
                        base_price = str(chosen_car.get_price()).strip()
                        order_conflict = self.order_ser.check_conflict(date1, date2, plate, order_id)
                    except Exception:
                        print("Wrong number input when choosing a car! Going back to main menu...")
                        break
                    if order_conflict == True:
                        client = self.client_menu(Client_ui())
                        if client == "q":
                            choice = "q"
                            break
                        name = client.name
                        lic_num = client.license_num
                        employee = self.employee_menu(Employee_UI())
                        employee_name = employee.get_name()
                        print("Mandatory base insurance added to order (12.000isk)")
                        price_duration = self.order_ser.find_base_price_with_duration(int(base_price), days_num)
                        print("Current total cost (with base insurance): ", price_duration)
                        insurance_price, insurance_list = self.order_ser.add_insurance_to_price()
                        final_price = price_duration + insurance_price
                        info_list = [order_id,date1,date2,plate,name,lic_num,employee_name, int(final_price), days_num]
                        print(info_list)
                        new_order = self.order_ser.create_order(info_list)
                        self.order_ser.add_order(new_order)
                        self.print_order(new_order,base_price,insurance_price,final_price,insurance_list)
                        self.order_ser.change_car_status(plate)
                        print("Order successfully registered into the database.\n")
                    else:
                        print("This car is already reserved during the dates input. Please find another car.")
                        print("")
                else:
                    print(explanation)
                    print("")

            elif choice == "2":
                keyword = self.choose_order()
                if keyword == "q":
                    print("Operation aborted.\n")
                else:
                    order_list = self.order_ser.find_order(keyword)
                    if order_list == []:
                        print("Order not found")
                    else:
                        found_id = order_list[0][0]
                        found_plate = order_list[0][3]
                        self.order_ser.change_car_status(found_plate)
                        self.order_ser.remove_order(found_id)
                        print("Order removed.\n")

            elif choice == "3":
                counter = 1
                order_list = self.order_ser.order_repo.get_all_orders()
                for item in order_list:
                    try:
                        item_list = item.split(",")
                        order_object = self.order_ser.create_order(item_list)
                        order_id = self.order_repo.order_model.get_order_id(order_object)
                        license_num = self.order_repo.order_model.get_plate(order_object)
                        client = self.order_repo.order_model.get_client_name(order_object)
                        start = self.order_repo.order_model.get_date_start(order_object)
                        end = self.order_repo.order_model.get_date_end(order_object)
                        price = self.order_repo.order_model.get_total_cost(order_object)
                        price = price[:-1]
                        print("{:>5d}. {}Order ID: {:>5s}{:>5s}License plate: {:>5s}{:>5s}Client: {:>5s} renting from {:>5s} to {:>5s} for a total of {:>5s}".format(counter,"|",order_id,"", license_num,"",client, start,end, price))
                        counter += 1
                    except Exception:
                        pass
                print("")
            
            elif choice == "4":
                order_not_found = True
                counter = 1
                order_list = self.order_ser.order_repo.get_all_orders()
                while order_not_found:
                    for item in order_list:
                        try:
                            item_list = item.split(",")
                            order_object = self.order_ser.create_order(item_list)
                            order_id = self.order_repo.order_model.get_order_id(order_object)
                            license_num = self.order_repo.order_model.get_plate(order_object)
                            client = self.order_repo.order_model.get_client_name(order_object)
                            start = self.order_repo.order_model.get_date_start(order_object)
                            end = self.order_repo.order_model.get_date_end(order_object)
                            price = self.order_repo.order_model.get_total_cost(order_object)
                            price = price[:-1]
                            print("{:>5d}. {}Order ID: {:>5s}{:>5s}License plate: {:>5s}{:>5s}Client: {:>5s} renting from {:>5s} to {:>5s} for a total of {:>5s}".format(counter,"|",order_id,"", license_num,"",client, start,end, price))
                            counter += 1
                        except Exception:
                            pass
                    print("")
                
                
                    order_id = input("Input id of order you want to change (ABC12): ")
                    found_order = self.order_repo.find_order(order_id)
                    if (type(found_order) == list and found_order != []):
                        order_not_found = False
                        nested_order_info = found_order
                        self.update_order(nested_order_info)
                    if found_order == []:
                        print("Order not found")
                    counter = 1
            else:
                print("Please enter a valid operation")

    def update_order(self,nested_order_info):
        print("1. Client\n2. Starting date\n3. Return date\n4. Car")
        choice = input("What would you like to update? (Please input integer choice): ")
        order_info = nested_order_info[0]
        old_order = order_info

        if choice == "1":
            client_info_list = Client_ui().client_op("4")
            if client_info_list != None:
                self.order_ser.change_client(client_info_list, old_order)
                        # client_not_found = False

            '''fer inni client_ui og gerir option4, læt option4 returna lista eða stakinu sem var breytt'''
            '''býr til nýtt order með nýju uppls. og eyðir því gamla'''

        elif choice == "2":
            new_date = input("New starting date (DD/MM/YYYY):\n ")
            is_start = True
            if self.order_ser.check_date_format(new_date) != None:
                new_order = self.order_ser.change_date(new_date, old_order, is_start)
                if new_order == None:
                    print("Invalid date inserted, example of date 1 1 2000")
            else:
                print("Invalid date inserted, example of date 1 1 2000")

        elif choice == "3":
            new_date = input("New return date (DD/MM/YYYY):\n ")
            is_start = False
            if self.order_ser.check_date_format(new_date) != None:
                new_order = self.order_ser.change_date(new_date, old_order, is_start)
                if new_order == None:
                    print("Invalid date inserted, example of date 1 1 2000")
            else:
                print("Invalid date inserted, example of date 1 1 2000")
        else:
            print("Invalid choice")


    def check_input(self, a_input, quit):
        try:
            new_inp = int(a_input)
            return new_inp
        except ValueError:
            if a_input == quit:
                return a_input
            else:
                return False
    
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

        print("\n","-"*86)
        print("RECEIPT:")
        print("Order id: {}\nEmployee: {}\n\nStarting date: {}\nReturn date: {}\n".format(self.order_id,self.employee_name,self.date_start,self.date_end))
        print("Car brand: {}\nCar type: {}\nCar plate: {}\n\nClient: {}\nDriver licence number: {}\n".format(self.car_brand,self.car_type,self.plate,self.client_name,self.licence_num))
        if insurance_list == "":
            print("No additional insurances")
        else:
            print("Chosen insurances: {}".format(insurance_list))
        print("Base insurance: {}\nBase car price: {}\nAdditional insurance cost: {}\n\nTotal price: {}\n".format(self.base_insurance,base_price,self.insurance_price,self.total_cost))
        print("-"*86,"\n")


