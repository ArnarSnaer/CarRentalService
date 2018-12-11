from models.car_model import Car

class Car_repository():
    def __init__(self):
        self.info = []
        self.car_model = Car

    def add_car(self, car):
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
        open_file = open("./data/vehicle.txt", "r")
        old_file = open_file.readlines()
        open_file.close()

        new_file = open("./data/vehicle.txt", "w")
        for line in old_file:
            if plate not in line:
                new_file.write(line)

        new_file.close()

    def find_car(self,searchword):
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
            info = line.split(",")
            if info[4] == True:
                avilable_cars.append(line)
            else:
                rented_cars.append(line)
        all_cars = [avilable_cars,rented_cars]
        return all_cars[choice]

    def get_all_cars(self):
        open_file = open("./data/vehicle.txt", "r")
        list_of_cars = open_file.readlines()
        open_file.close()

        return list_of_cars
