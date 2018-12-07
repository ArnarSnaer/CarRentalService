from models.car import Car

class CarRepo():
    def __init__(self):
        self.info = []

    def add_car(self):
        open_file = open("./data/cars.txt", "a")

        for item in self.info:
            to_write = str(item)
            open_file.write(to_write)
            if item != self.info[-1]:
                open_file.write(",")

        open_file.write("\n")

        open_file.close()

    def remove_car(plate):
        open_file = open("./data/cars.txt", "r")
        old_file = open_file.readlines()
        open_file.close()

        new_file = open("./data/cars.txt", "w")
        for line in old_file:
            if plate not in line:
                new_file.write(line)

        new_file.close()

    def find_car(searchword):
        open_file = open("./data/cars.txt", "r")
        
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
