from repositories.car_repo import Car_repository
#from models.car import Car


<<<<<<< HEAD
class Car_services:
=======
class Car_services(object):
>>>>>>> f95854d91ab91f012ba0e676561ba88868bd7ce7
    def __init__(self):
        self.car_repo = Car_repository()
        self.keywords = []

    def create_car(self,car_info):
        created_car = self.car_repo.Car(car_info[0],car_info[1],car_info[2],car_info[3],car_info[4],car_info[5],car_info[6],car_info[7])
        return created_car

    def list_to_formated_str(self,list):
        result_str = ""
        for item in list:
            if len(list) != 0:
                result_str += "\n"
            result_str += item

        return result_str
    
    def create_keyword_list(self):
        return self.keywords
    
    def add_keyword(self,keyword):
        return self.keywords.append(keyword)
    
    def rent_car(self,car_object):
        if car_object.get_status() == True:
            car_object.status = False
            

    def return_car(self,car_object):
        if car_object.get_status() == False:
            car_object.status  = True
    
    def get_available_cars(self):
        available_cars = self.car_repo.sort_cars(0)
        restults_str = self.list_to_formated_str(available_cars)
        return restults_str
    
    def get_rented_cars(self):
        rented_cars = self.car_repo.sort_cars(1)
        results_str = self.list_to_formated_str(rented_cars)
        return results_str

    def get_all_cars(self):
        results_txt = ""
        file_text = self.car_repo.get_all_cars()
        for line in file_text:
            if line == file_text[-1]:
                line = line.strip("\n")
            results_txt += line
        
        return results_txt

#hér vantar fall til að sjá hvort þessi bíll sé "VALID"
    def add_car(self, car):
        self.car_repo.add_car(car)
    
    def remove_car(self, car):
        self.car_repo.remove_car(car)
    
    