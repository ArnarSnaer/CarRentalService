class Creditcard(object):
    def __init__(self,name,address,phone,credit,duration,sec_num):
        self.name = name
        self.address = address
        self.phone = phone
        self.credit = credit
        self.duration = duration
        self. sec_num = sec_num
        self.info = [self.name, self.address,self.phone,self.credit,self.duration,self.sec_num]
    
    def __str__(self):
        return str(self.info)
    
    def __getitem__(self,index):
        return self.info[index]
    
    def __iter__(self):
        return iter(self.info)
    

#thing = Creditcard("Ari","Gullfoss 2", 5812345, "5555 5555 5555 5555", "10/21", "123")
#print(thing[3])

#for item in thing:
 #   print(item)
