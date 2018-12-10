from repositories.car_repo import Car_repository
#from models.car import Car


class Car_services(object):
    def __init__(self):
        self.car_repo = Car_repository()
        self.keywords = []

    def create_car(self,car_info):
        #car_list = []
        created_car = Car(car_info[0],car_info[1],car_info[2],car_info[3],car_info[4],car_info[5],car_info[6],car_info[7])
        #car_list.append(created_car)
        return created_car

    def list_to_formated_str(self,list):
        result_str = ""
        for item in list:
            result_str += item
            if item != list[-1]:
                result_str += "\n"
        return result_str
    
    def create_keyword_list(self):
        return self.keywords
    
    def add_keyword(self,keyword):
        return self.keywords.append(keyword)
    
    def rent_car(self,car):
        if car.status == True:
            car.sstatus = False

    def return_car(self,car):
        if car.status == False:
            car.status  = True
    
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
    
    
