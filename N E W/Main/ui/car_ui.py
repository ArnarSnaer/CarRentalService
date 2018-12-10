from services.car_services import Car_services

class Car_UI(object):

    def __init__(self):
        self.car_serv = Car_services()
    
    def choose_car(self,results):
        number = 1
        for item in results:
            print("{}. {}".format(number,item))
        choice = int(input("Select a car: "))
        chosen_car = results[choice-1]
        return chosen_car
    
    def car_menu(self):
        choice = ""

        while choice != "q":
            print("What would you like to do?\n1. Rent car\n2. Return car\n3. Find a cars information\4. Get a list of cars\nq. Quit")
            choice = input("What would you like to do? ").lower()
            
            if choice == "1":
                print(self.car_serv.get_available_cars())
                
            elif choice == "2":
                print(self.car_serv.get_rented_cars())

            elif choice == "3":
                pass
            elif choice == "4":
                pass

car1 = Car_UI()
car1.car_menu()