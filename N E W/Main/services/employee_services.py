from models.employee import Employee

class Employee_services(object):
    def __init__(self,name):
        self.name = name
        self.employee = Employee(name)

    def add_sale(self,other): #Þetta færir order, gerð bílsins eða bílnumer...
        try:
            return self.employee.name.append(other)
        except ValueError:
            return "> Sale not found, try again"
        
    def remove_sale(self,other):
        try:
            return self.employee.name.remove(other)
        except ValueError:
            return "> Plate not found in sales"

    def get_sales(self):
        employee_order = ""
        for item in self.employee.name[1:]:
            if item != self.employee.name[-1]:
                employee_order += item + "\n"
            else:
                employee_order += item

        if employee_order == "":
            return "> No sales"
        else:
            return employee_order
    
    def change_name(self,new_name):
        self.employee.name[0] = new_name
        return self.employee
        
#Gunnar = Employee_services("Gunnar")
#Gunnar_v2 = Employee_services()
#Gunnar.add_sale("Skoda")
#Gunnar.add_sale("Ferrari")
#Gunnar.add_sale("Toyota")
#Gunnar.remove_sale("Ferrari")
#print(Gunnar.get_sales())