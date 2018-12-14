from services.calc_services import Calculator_services
import os

class Calc_UI(object):

    def __init__(self):
        self.calc_serv = Calculator_services()

    def calc_menu(self):
        choice = ""
        os.system('cls')


        while choice != "q":
            print("Current section: Calculator\n1. Find price of specific car type\nq. Back")
            choice = input("> What would you like to do? ")
            if choice == "1":
                veh_type = input("Which vehicle type should be chosen?\n1. SUV\n2. Sedan\n3. MPV\n4. Mini\n5. Sport\n> Write with the respective integer:")
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
                result = self.calc_serv.find_price(chosen, veh_dur)
                if result == 0:
                    print("Something went wrong! You may have input something incorrect. Try again.\n")
                else:
                    print("Your setup would cost: {} ISK\n".format(result))
