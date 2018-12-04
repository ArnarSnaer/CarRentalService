#from Order import Order
class Employee():
    def __init__(self):
        self.textfile = "employees.txt"
        self.employee_list = []

    def new_list(self):
        open_file = open(self.textfile, "r")
        for name in open_file:
            name = name.replace("\n","")
            self.employee_list.append(name)

        open_file.close()
        
        return self.employee_list

  #  def __repr__(self):
   #     return
    
    def __str__(self):
        return str(self.employee_list)
        
test = Employee()
employee_list = test.new_list()
print(employee_list)
