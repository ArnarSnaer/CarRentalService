from repositories.car_repo import Car_repository

class Car_services(object):
    def __init__(self):
        self.car_repo = Car_repository()
        self.car_model = self.car_repo.car_model()
        self.keywords = []
        self.veh_type = self.car_model.veh_type #Finnur ekki veh_type

        price_dict = {"suv": 100000, "mini": 10000, "mpv": 50000, "sport": 200000,"sedan": 75000}
        self.veh_type = self.veh_type.lower() 
        self.price = 0
        for key, value in price_dict.items(): 
            if key == self.veh_type in price_dict:
                self.price = value
                self.car_repo.car_model.price = value #Verð verður að tölu

    def create_car(self,car_info):
        created_car = self.car_repo.car_model(car_info[0],car_info[1],car_info[2],car_info[3],car_info[4],car_info[5],car_info[6],car_info[7],car_info[8])
        return created_car

    def create_car_from_list(self, car_list): #Frá streng? afh er split()??
        car_info = car_list.split(",")
        created_car = self.car_repo.car_model(car_info[0],car_info[1],car_info[2],car_info[3],car_info[4],car_info[5],car_info[6],car_info[7],car_info[8])
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
    
    # def all_available_cars(self, choice):
    #     results_txt = ""
    #     file_text = self.car_repo.get_all_cars()
    #     number = 1
    #     for item in file_text:
    #         car_object = self.create_car_from_list(item)
    #         veh_type = self.car_repo.car_model.get_veh_type(car_object)
    #         brand = self.car_repo.car_model.get_brand(car_object)
    #         plate = self.car_repo.car_model.get_plate(car_object)
    #         price = self.car_repo.car_model.get_price(car_object)
    #         price = price[:-1]
    #         if choice == "4":
    #             if self.car_repo.car_model.get_status(car_object) == "True":
    #                 status = "Available."
    #             else:
    #                 status = "Unavailable."
    #             print("{:>5d}. {} Type: {:>5s}{:>5s}Brand: {:>5s}{:>5s}License plate: {:>5s}{:>5s}Base price: {:>5s}{:<5s}Current status: {:>5s}".format(number,"|",veh_type,"", brand,"", plate,"", price,"", status))
    #             number += 1
    #         elif choice == "5":
    #             if self.car_repo.car_model.get_status(car_object) == "True":
    #                 status = "Available."
    #                 print("{:>5d}. {} Type: {:>5s}{:>5s}Brand: {:>5s}{:>5s}License plate: {:>5s}{:>5s}Base price: {:>5s}{:<5s}Current status: {:>5s}".format(number,"|",veh_type,"", brand,"", plate,"", price,"", status))
    #                 number += 1
    #         elif choice == "6":
    #             if self.car_repo.car_model.get_status(car_object) == "False":
    #                 status = "Unavailable."
    #                 print("{:>5d}. {} Type: {:>5s}{:>5s}Brand: {:>5s}{:>5s}License plate: {:>5s}{:>5s}Base price: {:>5s}{:<5s}Current status: {:>5s}".format(number,"|",veh_type,"", brand,"", plate,"", price,"", status))
    #                 number += 1
    #     return results_txt

    def get_available_cars(self):
        available_cars = self.car_repo.sort_cars(0)
        restults_str = self.list_to_formated_str(available_cars)
        return restults_str

    def get_available_cars_list(self):
        available_cars = self.car_repo.sort_cars(0)
        real_list = []
        for item in available_cars:
            item = item.split(",")
            real_list.append(item)
        return real_list
    
    def get_rented_cars(self):
        rented_cars = self.car_repo.sort_cars(1)
        results_str = self.list_to_formated_str(rented_cars)
        return results_str

    def calculate_price(self, choice):
        try:
            price_dict = {"suv": 100000, "hatchback": 50000, "sedan": 50000, "sport": 200000,"mpv": 75000, "crossover": 75000, "convertible": 200000}
            price = 0
            choice = choice.lower()
            print(choice)
            for key, value in price_dict.items():
                if choice == key:
                    price = value
            
        except Exception:
            price = 0

        return price

    def get_status(self):
        return self.car_model.get_status()

