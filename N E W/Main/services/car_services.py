from repositories.car_repo import Car_repository

class Car_services(object):
    def __init__(self):
        self.car_repo = Car_repository()
        self.car_model = self.car_repo.car_model()
        self.keywords = []
        self.veh_type = self.car_model.veh_type 

        self.VEH_TYPE = 0
        self.BRAND = 1
        self.PLATE = 2
        self.WHEEL_DRIVE = 3
        self.STATUS = 4
        self.IS_MANUAL = 5
        self.DRIVEN = 6
        self.FUEL_TYPE = 7
        self.PRICE = 8

        price_dict = {"suv": 100000, "mini": 10000, "mpv": 50000, "sport": 200000,"sedan": 75000}
        self.veh_type = self.veh_type.lower() 
        self.price = 0
        for key, value in price_dict.items(): 
            if key == self.veh_type in price_dict:
                self.price = value
                self.car_repo.car_model.price = value 

        

    def create_car(self,car_info):
        created_car = self.car_repo.car_model(car_info[self.VEH_TYPE],car_info[self.BRAND],car_info[self.PLATE],car_info[self.WHEEL_DRIVE],car_info[self.STATUS],
                                                car_info[self.IS_MANUAL],car_info[self.DRIVEN],car_info[self.FUEL_TYPE],car_info[self.PRICE])
        return created_car

    def create_car_from_list(self, car_list): 
        car_info = car_list.split(",")
        created_car = self.car_repo.car_model(car_info[self.VEH_TYPE],car_info[self.BRAND],car_info[self.PLATE],car_info[self.WHEEL_DRIVE]
                        ,car_info[self.STATUS],car_info[self.IS_MANUAL],car_info[self.DRIVEN],car_info[self.FUEL_TYPE],car_info[self.PRICE])
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
        if split_list[self.STATUS] == "True":
            split_list[self.STATUS] = "False" 
        else:
            split_list[self.STATUS] = "True"
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
            price_dict = {"suv": 100000, "mini": 50000, "sedan": 50000, "sport": 200000,"mpv": 75000}
            price = 0
            choice = choice.lower()
            for key, value in price_dict.items():
                if choice == key:
                    price = value
            
        except Exception:
            price = 0

        return price
            