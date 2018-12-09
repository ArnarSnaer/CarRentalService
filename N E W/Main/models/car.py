''' A car's status is in Boolean-form
    A car's available if status is True and is out in rent when status =             
    False'''
    
#ATH að velja kostnað fyrir veh_type
class Car(object):
    def __init__(self, veh_type, brand, plate, wheel_drive, status, is_manual, driven, fuel_type, price = 0): #Kannski records
        self.veh_type = veh_type
        self.brand = brand
        self.plate = plate
        self.wheel_drive = wheel_drive
        self.status = status
        self.is_manual = is_manual
        self.driven = driven
        # self.records = records
        self.fuel_type = fuel_type
        self.price = price
        self.info = [self.veh_type, self.brand, self.plate, self.wheel_drive, self.status, self.is_manual, self.driven, self.fuel_type, self.price]
    
    def __str__(self):
        return str(self.info)
    
    def __getitem__(self,index_num):
        return self.info[index_num]
    
    def __iter__(self):
        return iter(self.info)


    #def get_rent_history(self): Vinna í seinna, vantar .txt 
    
    def get_info(self):
        return "Vehicle type: {}\nBrand: {}\nPlate number: {}\nWheel drive: {}\nStatus: {}\nGear box: {}\nDriven {}\nFuel type: {}\nPrice: {}".format(self.veh_type, self.brand, self.plate,self.wheel_drive, self.status, self.is_manual, self.driven, self.fuel_type, self.price)
    

    def get_type(self):
        return self.info[1]

    def get_plate(self):
        return self.info[2]

    def get_price(self):
        return self.price
       

            
'''    
bill = Car("MPV","Toyota Land Cruiser","ER C01","4x4",True,False,60000,"diesel")
value = bill.check_price()
print(value)
print(bill)
print(bill.get_info())
print(bill.get_status())
'''