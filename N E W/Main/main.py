from ui.car_ui import Car_UI

class Main(object):
    def __init__(self):
        car_ui = Car_UI()
    
    def main_menu(self):
        choice = ""
        while choice != "e":
            choice = input("What would you like to do?\n ").lower()

            if choice == "1":
                car_ui.car_menu()
