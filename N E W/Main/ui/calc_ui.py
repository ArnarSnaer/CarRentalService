from services.calc_services import Calculator_services
import os

class Calc_UI(object):
    def __init__(self):
        self.calc_serv = Calculator_services()

    def calc_menu(self): 
        '''Calculator that shows the base price of a chosen car, with added insurances'''
        choice = ""
        os.system('cls')

        while True:
            print("Current section: Calculator\n1. Find price of specific car type\nq. Back")
            choice = input("> What would you like to do? ")
            if choice == "1":
                veh_type = input("Which vehicle type should be chosen?\n1. SUV\n2. Sedan\n3. MPV\n4. Mini\n5. Sport\n> Write with the respective integer: ")
                if (veh_type == "1") or (veh_type == "SUV"):
                    chosen = "suv"
                elif veh_type == "2" or (veh_type == "Sedan"):
                    chosen = "sedan"
                elif veh_type == "3" or (veh_type == "MPV"):
                    chosen = "mpv"
                elif veh_type == "4" or (veh_type == "Mini"):
                    chosen = "mini"
                elif veh_type == "5" or (veh_type == "Sport"):
                    chosen = "sport"
                else:
                    chosen = ""
                veh_dur = input("> For how long will the car be rented? Answer in days: ")
                total_price_no, total_price_with, base_price = self.calc_serv.find_price(chosen, veh_dur)
                print("Base insurance is always added to a car's rental.")
                print("Car type's base price: {}\nPrice when rented for {} days:\n - With base insurance: {}\n - Without base insurance: {}\n".format(base_price, veh_dur, total_price_with, total_price_no))
                print("Insurance types:\n1. Water Damage Collision: 10'000 ISK\n2. CASCO Insurance: 20'000 ISK\n3. Some Other Insurance: 5'000 ISK")
                if total_price_no == 0:
                    print("Something went wrong! You may have input something incorrect. Try again.\n")
                else:
                    print("\nYour setup would cost: {} ISK\n".format(total_price_with))
            
            if (choice == "q") or (choice == "Q"):
                print("Going back to main menu...\n")
                break
