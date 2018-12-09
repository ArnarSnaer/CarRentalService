from models.car import Car

class CarRepo():
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

    def remove_car(self, plate):
        open_file = open("./data/vehicle.txt", "r")
        lines = open_file.readlines()
        open_file.close()

        open_file = open("./data/vehicle.txt", "w")
        for line in lines:
            if plate not in line:
                open_file.write(line)

        open_file.close()

    def find_car(self, searchword):
        open_file = open("./data/vehicle.txt", "r")
        
        for line in open_file:
            if searchword in line:
                found_list = line.split()
                print(found_list)

'''
test_car = Car("Sport", "Ferrari", "ABC12", "4x4", "True", "False", "12000", "Diesel")
CarRepo.add_car(test_car)
plate_to_remove = "ABC12"
carToFind = input("What car to delete? ")
CarRepo.find_car(carToFind)
'''
