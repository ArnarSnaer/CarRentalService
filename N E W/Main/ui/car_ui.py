from services.car_services import Car_services

class Car_UI(object):

    def __init__(self):
        self.car_serv = Car_services()
        self.car_repo = self.car_serv.car_repo
        self.keywords = []
    
    def choose_car(self,results):
        number = 1
        for item in results:
            car_object = self.car_serv.create_car(item)
            veh_type = self.car_repo.car_serv.Get.get_veh_type(car_object)
            brand = self.car_repo.Car.get_brand(car_object)
            plate = self.car_repo.Car.get_plate(car_object)
            if self.car_repo.Car.get_status(car_object) == "True":
                status = "Available."
            else:
                status = "Unavailable."
            print("{}. Type: {} Brand: {} License plate: {} Current status: {}".format(number,veh_type, brand, plate, status))
            number += 1
        print("Complete! Here are all the results of the search.")
        choice = int(input("Choose a car: ")
        return results[choice-1]
    
    def car_menu(self):
        choice = ""

        while choice != "q":
            print("Current section: Cars\n1. Rent car\n2. Return car\n3. Search car database\n4. See all cars\nq. Quit")
            choice = input("> What would you like to do? ").lower()
            
            if choice == "1":
                #print(self.car_serv.get_available_cars())
                plate = input("> Enter the license plate of desired car: ")
                results = self.car_repo.find_car(plate)

                if len(results) != 0:
                    self.choose_car(results)
                    choice = int(input("> Select a car: "))
                    chosen_car = results[choice-1]
                    created_car = self.car_serv.create_car(chosen_car)
                    rent_status = self.car_repo.Car.get_status(created_car)

                    if rent_status == "False":
                        print("This car is not available for renting. Please find another.\n")
                    elif rent_status == "True":
                        result = self.car_serv.rent_car(created_car)
                        self.car_repo.remove_car(plate)
                        changed_status = self.car_serv.create_car_from_list(result)
                        self.car_repo.add_car(changed_status)
                        print("Complete! The car has been updated to an 'unavailable' status!\n")

                else:
                    print("No match.\n")

            elif choice == "2":
                plate = input("> Enter the license plate of desired car: ")
                results = self.car_repo.find_car(plate)

                if len(results) != 0:
                    self.choose_car(results)
                    choice = int(input("> Select a car: "))
                    chosen_car = results[choice-1]
                    created_car = self.car_serv.create_car(chosen_car)
                    rent_status = self.car_repo.Car.get_status(created_car)

                    if rent_status == "True":
                        print("This car is available and doesn't need returning.\n")
                    elif rent_status == "False":
                        result = self.car_serv.rent_car(created_car)
                        self.car_repo.remove_car(plate)
                        changed_status = self.car_serv.create_car_from_list(result)
                        self.car_repo.add_car(changed_status)
                        print("Complete! The car has been returned and is 'available' again!\n")

                else:
                    print("No match.\n")

            elif choice == "3":                
                searchword = input("> Insert information as search word; Vehicle type, Brand, License plate, etc\nPlease only enter a single item:  ")
                results = self.car_repo.find_car(searchword)
                if len(results) == 0:
                    print("No results for this search word.")
                else:
                    self.choose_car(results)

            elif choice == "4":
                print(self.car_serv.get_all_cars())
            
            elif choice != "q":
                print("Invalid input! Please enter the number/letter in front of each operation!")


    def order_menu(self):
        print("Available car:\n")
        available_cars = self.car_serv.get_available_cars_list()
        chosen_car = self.choose_car(available_cars)
        rented_car = self.car_repo.car_serv.create_car(chosen_car)
        return rented_car
            
