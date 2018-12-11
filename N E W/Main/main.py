from ui.calc_ui import Calc_UI
from ui.car_ui import Car_UI

def main():
    print("Welcome, User")
    choice = ""

    while choice != "5": 
        print("Available sections:\n1. Order\n2. Cars\n3. Client\n4. Calculator\n5. Exit program")
        choice = input("> Choose a section: ")
        if choice == "1":
            print("work in progress, please hold")
        elif choice == "2":
            car_UserInterface = Car_UI()
            car_UserInterface.car_menu()
        elif choice == "3":
            print("work in progress, please hold")
        elif choice == "4":
            calc_UserInterface = Calc_UI()
            calc_UserInterface.calc_menu()      
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid input!")      
                        

main()
