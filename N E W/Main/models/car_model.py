 #ATH að velja kostnað fyrir veh_type
class Car(object):
    def __init__(self, veh_type="", brand="", plate="", wheel_drive="", status="", is_manual="", driven="", fuel_type="", price = 0): #Kannski records
        self.veh_type = veh_type
        self.brand = brand
        self.plate = plate
        self.wheel_drive = wheel_drive
        self.status = status
        self.is_manual = is_manual
        self.driven = driven
        self.fuel_type = fuel_type
        self.price = price
        
    
    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}".format(self.veh_type, self.brand, self.plate, self.wheel_drive, self.status, self.is_manual, self.driven, self.fuel_type, self.price)

    def get_veh_type(self):
        return self.veh_type

    def get_brand(self):
        return self.brand

    def get_plate(self):
        return self.plate

    def get_wheel_drive(self):
        return self.wheel_drive

    def get_status(self):
        return self.status

    def get_is_manual(self):
        return self.is_manual
    
    def get_driven(self):
        return self.driven

    def get_fuel_type(self):
        return self.fuel_type

    def get_price(self):
        return self.price
