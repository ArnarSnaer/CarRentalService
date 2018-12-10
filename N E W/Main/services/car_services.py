from repositories.car_repo import Car_repository
from models.car import Car


class Car_services(object):
    def __init__(self):
        self.__car_repo = Car_repository()

    def create_car(self,car_info):
        car_list = []
        created_car = Car(car_info[0],car_info[1],car_info[2],car_info[3],car_info[4],car_info[5],car_info[6],car_info[7])
        car_list.append(created_car)
        return car_list

    def list_to_formated_str(self,list):
        result_str = ""
        for item in list:
            result_str += item
            if item != list[-1]:
                result_str += "\n"
        return result_str
    
    def rent_car(self,car):
        if car.status == True:
            car.sstatus = False

    def return_car(self,car):
        if car.status == False:
            car.status  = True
    
    def get_available_cars(self):
        



#hér vantar fall til að sjá hvort þessi bíll sé "VALID"
    def add_car(self, car):
        self.__car_repo.add_car(car)
    
    def remove_car(self, car):
        self.__car_repo.remove_car(car)
    
    
