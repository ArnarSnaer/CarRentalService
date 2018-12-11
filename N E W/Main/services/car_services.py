from repositories.car_repo import Car_repository
#from models.car import Car

class Car_services(object):
    def __init__(self):
        self.car_repo = Car_repository()
        self.keywords = []

    def create_car(self,car_info):
        created_car = self.car_repo.Car(car_info[0],car_info[1],car_info[2],car_info[3],car_info[4],car_info[5],car_info[6],car_info[7])
        return created_car

    def create_car_from_list(self, car_list): #Frá streng? afh er split()??
        car_info = car_list.split(",")
        created_car = self.car_repo.Car(car_info[0],car_info[1],car_info[2],car_info[3],car_info[4],car_info[5],car_info[6],car_info[7])
        return created_car

    def list_to_formated_str(self,list):
        result_str = ""
        if len(list) == 0:
            return "No matches!"
        else:
            for item in list:
                if "\n" in item:
                    item = item[:-1]
                else:
                    item += ","
                result_str += item
            return result_str
    
    def create_keyword_list(self):
        return self.keywords
    
    def add_keyword(self,keyword):
        return self.keywords.append(keyword)
    
    def rent_car(self,car_object):
        car_object = str(car_object)
        split_list = car_object.split(",")
        if split_list[4] == "True":
            split_list[4] = "False" # Er hægt að stytta, einhver með fleiri brain cells að laga
        else:
            split_list[4] = "True"
        new_str = ""
        for item in split_list:
            new_str += item
            if item == split_list[-1]:
                new_str += "\n"
            else:
                new_str += ","
        return new_str

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
        number = 1
        for line in file_text:
            car = self.create_car_from_list(line)
            veh_type = self.car_repo.Car.get_veh_type(car)
            brand = self.car_repo.Car.get_brand(car)
            plate = self.car_repo.Car.get_plate(car)
            if self.car_repo.Car.get_status(car) == "True":
                status = "Available."
            else:
                status = "Unavailable."
            print("{}. Type: {} Brand: {} License plate: {} Current status: {}".format(number,veh_type, brand, plate, status))
            number += 1
        
        return results_txt
