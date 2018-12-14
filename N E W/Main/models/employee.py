class Employee(object):
    def __init__(self,name=""):
        self.name = []
        self.name.append(name)
    
    def __str__(self):
        return "{}".format(self.name[1:])
    
    def __getitem__(self,index):
        return 

    def get_name(self):
        return "{}".format(self.name[0])
    
