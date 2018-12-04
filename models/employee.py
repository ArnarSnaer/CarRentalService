#from Order import Order
class Employee(object):
    def __init__(self,name):
        self.name = []
        self.name.append(name)
        #self.file = open("employee_list.txt", r+)
    
    def __str__(self):
        return "{}".format(self.name[1:])
    
    def get_name(self):
        return "{}".format(self.name[0])
    
    def add_sale(self,other): #Þetta færir order, gerð bílsins eða bílnumer...
        return self.name.append(other)

gunnar = Employee("Gunnar")
gunnar.add_sale("Honda civic 2014")
print(gunnar)
nafn = gunnar.get_name()
print(nafn)