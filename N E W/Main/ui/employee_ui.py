from models.employee import Employee

class Employee_UI(object):
    def init(self):
        self.employee = Employee()

    def order_menu(self):
        '''Menu used for the Order UI'''
        employee_name = input("Enter employee name: ")
        working_employee = Employee(employee_name)
        return working_employee