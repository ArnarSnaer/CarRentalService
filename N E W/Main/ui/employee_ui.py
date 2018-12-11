from services.employee_services import Employee_services
from models.employee import Employee

class Employee_UI(object):
    def __init__(self,name):
        self.name = name
        self.employee_ser = Employee_services(name)
        self.employee = Employee(name)
    
    def print_sales(self):
        print(self.employee_ser.get_sales())

    def __str__(self):
        return "{}".format(self.name)
    
    def employee_menu(self):
        choice = ""
        while(choice != "q"):
            print("What would you like to do?\n1. Add sale\n2. Remove sale\n3. Get a list of all sales\nq. Quit")
            choice = input("What would you like to do? ").lower()

            if choice == "1":
                sale = input("Input license plate of rented car: ")
                self.employee_ser.add_sale(sale)
            
            elif choice == "2":
                sale = input("Input license plate of rented car: ")
                self.employee_ser.remove_sale(sale)
            
            elif choice == "3":
                self.print_sales()
            
            else:
                print("Please insert valid choice.")
            
            

    def order_menu(self):
        employee_name = input("Enter employee name: ")
        working_employee = Employee(employee_name)
        return working_employee
        
Gunnar = Employee_UI("Gunnar")
Gunnar.employee_menu()