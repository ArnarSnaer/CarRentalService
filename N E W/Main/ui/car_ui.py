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
            print("{}. {}".format(number,car_object))
            number += 1
        choice = int(input("Select a car: "))
        chosen_car = results[choice-1]
        return chosen_car
    
    def car_menu(self):
        choice = ""

        while choice != "q":
            print("What would you like to do?\n1. Rent car\n2. Return car\n3. Find a cars information\n4. Get a list of cars\nq. Quit")
            choice = input("What would you like to do? ").lower()
            
            if choice == "1":
                print(self.car_serv.get_available_cars())
                plate = input("Enter the license plate of desired car: ")
                results = self.car_repo.find_car(plate)

                if len(results) != 0:
                    chosen_car = self.choose_car(results)
                    created_car = self.car_serv.create_car(chosen_car)

                    self.car_repo.remove_car(created_car.plate)
                    self.car_serv.rent_car(created_car)
                    self.car_repo.add_car(created_car)
                else:
                    print("No match.\n")

            elif choice == "2":
                print(self.car_serv.get_rented_cars())
                plate = input("Enter the license plate of desired car: ")
                results = self.car_repo.find_car(plate)

                if len(results) != 0:
                    chosen_car = self.choose_car(results)
                    created_car = self.car_serv.create_car(chosen_car)

                    self.car_repo.remove_car(created_car.plate)
                    self.car_serv.return_car(created_car)
                    self.car_repo.add_car(created_car)
                else:
                    print("No match.\n")

            elif choice == "3":
                keywords = self.car_serv.create_keyword_list()                
                while choice != "s":
                    choice = input("Insert information as searchkey and type 's' to search ")
                    if choice != "s":                    
                        self.car_serv.add_keyword(choice)
                results = self.car_repo.find_car(keywords)
                print(results)

            elif choice == "4":
                print(self.car_serv.get_all_cars())

#car1 = Car_UI()
#car1.car_menu()