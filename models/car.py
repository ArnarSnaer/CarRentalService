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
    
        price_dict = {"jeppi": 100000, "smábíll": 10000, "smárúta": 50000, "sportbíll": 200000,"fólksbíll": 75000}
        self.veh_type = self.veh_type.lower() 
        self.price = 0
        for key, value in price_dict.items(): 
            if key == self.veh_type in price_dict:
                self.price = value
                self.info[-1] = value
        

    def __str__(self):
        return str(self.info)
    
    def __getitem__(self,index_num):
        return self.info[index_num]
    
    def get_type(self):
        return self.info[1]
    
    def get_plate(self):
        return self.info[2]
    
    def __iter__(self):
        return iter(self.info)    
    
    def rent(self):
        self.status = False
    
    #def get_rent_history(self): Vinna í seinna, vantar .txt 
    
    def get_status(self):
        if self.status == True:
            return "This car is available."
        else:
            return "This car is not available"
            
    def get_info(self):
        return "Vehicle type: {}\nBrand: {}\nPlate number: {}\nWheel drive: {}\nStatus: {}\nGear box: {}\nDriven {}\nFuel type: {}\nPrice: {}".format(self.veh_type, self.brand, self.plate,self.wheel_drive, self.status, self.is_manual, self.driven, self.fuel_type, self.price)
    
    def return_vehicle(self):
        self.status = True
    
    def get_price(self):
        return self.price
    
    def add_car(self):
        open_file = open("cars.txt", "a")

        for item in self.info:
            to_write = str(item)
            open_file.write(to_write)
            if item != self.info[-1]:
                open_file.write(",")

        open_file.write("\n")

        open_file.close()

    def remove_car(plate):
        open_file = open("cars.txt", "r")
        old_file = open_file.readlines()
        open_file.close()

        new_file = open("cars.txt", "w")
        for line in old_file:
            if plate not in line:
                new_file.write(line)

        new_file.close()

    def check_price(self):
        price_dict = {"suv": 100000, "hatchback": 50000, "sedan": 50000, "sport": 200000,"mpv": 75000, "crossover": 75000, "convertible": 200000}
        self.veh_type = self.veh_type.lower() 
        self.price = 0
        for key, value in price_dict.items(): 
            if key == self.veh_type in price_dict:
                self.price = value
                self.info[-1] = value
        
        return self.price
       
'''
bill = Car("MPV","Toyota Land Cruiser","ER C01","4x4",True,False,60000,"diesel")
value = bill.check_price()
print(value)
print(bill)
print(bill.get_info())
print(bill.get_status())
# veh_type, brand, plate, wheel_drive, status, is_manual, driven, fuel_type
# Attempting to add a car to a .txt file
vehicle_type = input("Vehicle type: ")
car_brand = input("Car brand: ")
car_plate = input("Car plate: ")
car_drive = input("Car wheel drive: ")
car_status = True
car_manual = False
car_driven = input("How much has the car been driven? Answer with an integer: ")
car_fuel_type = input("What is the car's fuel type? ")
new_car = Car(vehicle_type, car_brand, car_plate, car_drive, car_status, car_manual, car_driven, car_fuel_type)
new_car.check_price()
new_car.add_car()

old_car = input("Enter the plate of the car you wish to remove: ")
Car.remove_car(old_car)
'''