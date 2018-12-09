from repositories.car_repo import CarRepo

class Car_services:
    def __init__(self):
        self.__car_repo = CarRepo()


#hér vantar fall til að sjá hvort þessi bíll sé "VALID"
    def add_car(self, car):
        self.__car_repo.add_car(car)
    
    def remove_car(self, car):
        self.__car_repo.remove_car(car)
    
    