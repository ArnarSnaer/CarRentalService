from models.car_model import Car

class Car_repository():
    def __init__(self):
        self.info = []
        self.car_model = Car

    def add_car(self, car):
        '''Adds a car to the database'''
        open_file = open("./data/vehicle.txt", "a")

        veh_type = car.get_veh_type()
        brand = car.get_brand()
        plate = car.get_plate()
        wheel_drive = car.get_wheel_drive()
        status = car.get_status()
        is_manual = car.get_is_manual()
        driven = car.get_driven()
        fuel_type = car.get_fuel_type()
        price = car.get_price()
        open_file.write("{},{},{},{},{},{},{},{},{}\n".format(veh_type, brand, plate, wheel_drive, status, is_manual, driven, fuel_type, price))

        open_file.close()

    def remove_car(self,plate):
        ''' Removes a car from database'''
        open_file = open("./data/vehicle.txt", "r")
        old_file = open_file.readlines()
        open_file.close()

        new_file = open("./data/vehicle.txt", "w")
        for line in old_file:
            if line == "\n":
                new_file.write("")
            elif plate not in line:
                new_file.write(line)

        new_file.close()

    def find_car(self,searchword):
        '''Finds a car and returns it in a list form, or returns an empty list if the car is not there'''
        open_file = open("./data/vehicle.txt", "r")
        car_list = []
        for line in open_file:
            if searchword in line:
                found_list = line.split(",")
                car_list.append(found_list)
        
        return car_list
    
    def sort_cars(self,choice):
        open_file = open("./data/vehicle.txt", "r")
        avilable_cars = []
        rented_cars = []
        all_cars = []
        for line in open_file:
            try:
                info = line.split(",")
                if info[4] == "True":
                    avilable_cars.append(line)
                else:
                    rented_cars.append(line)
            except Exception:
                pass
        all_cars = [avilable_cars,rented_cars]
        return all_cars[choice]

    def get_all_cars(self):
        open_file = open("./data/vehicle.txt", "r")
        list_of_cars = open_file.readlines()
        open_file.close()

        return list_of_cars
