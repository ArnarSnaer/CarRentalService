from services.calc_services import Calculator_services

class Calc_UI(object):

    def __init__(self):
        self.calc_serv = Calculator_services()

    def calc_menu(self):
        choice = ""

        while choice != "q":
            print("Current section: Calculator\n1. Find price of specific car type\nq. Back")
            choice = input("> What would you like to do? ")
            if choice == "1":
                veh_type = input("Which vehicle type should be chosen?\n1. SUV\n2. Sedan\n3. MPV\n> Write with the respective integer:")
                if veh_type == "1":
                    chosen = "suv"
                elif veh_type == "2":
                    chosen = "sedan"
                elif veh_type == "3":
                    chosen = "mpv"
                else:
                    chosen = ""
                veh_dur = input("> For how long will the car be rented? Answer in days: ")
                result = self.calc_serv.find_price(chosen, veh_dur)
                if result == 0:
                    print("Something went wrong! You may have input something incorrect. Try again.\n")
                else:
                    print("Your setup would cost: {} ISK\n".format(result))
