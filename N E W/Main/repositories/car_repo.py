from models.car import Car

class Car_repository():
    def __init__(self):
        self.info = []

    def add_car(self):
        open_file = open("./data/vehicle.txt", "a")

        for item in self.info:
            to_write = str(item)
            open_file.write(to_write)
            if item != self.info[-1]:
                open_file.write(",")

        open_file.write("\n")

        open_file.close()

    def remove_car(self,plate):
        open_file = open("./data/cars.txt", "r")
        old_file = open_file.readlines()
        open_file.close()

        new_file = open("./data/cars.txt", "w")
        for line in old_file:
            if plate not in line:
                new_file.write(line)

        new_file.close()

    def find_car(self,searchword):
        open_file = open("./data/cars.txt", "r")
        car_list = []
        for line in open_file:
            if searchword in line:
                found_list = line.split()
                car_list.append(found_list)
        return car_list
    
    def sort_cars(self):
        open_file = open("./data/cars.txt", "r")
        avilable_cars = []
        rented_cars = []
        for line in open_file:
            info = line.split(",")
            if info[4] == True:
                avilable_cars.append(line)
            else:
                rented_cars.append(line)

        return avilable_cars,rented_cars
 
