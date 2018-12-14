from models.employee import Employee
import os

class Employee_UI(object):
    def init(self):
        self.employee = Employee()

    def order_menu(self):
        os.system('cls')
        employee_name = input("Enter employee name: ")
        working_employee = Employee(employee_name)
        return working_employee