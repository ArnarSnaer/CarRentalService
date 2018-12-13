from ui.calc_ui import Calc_UI
from ui.car_ui import Car_UI
from ui.order_ui import Order_UI
from ui.client_ui import Client_ui
from models.order_model import Order

def main():
    print("Welcome, User")
    choice = ""
    
    pontun = Order("AAA11","12 5 2018","15 5 2018","ANC71","Peter","Gunnar",1000,4)
    Order_UI().print_order(pontun)

    while choice != "5": 
        print("Available sections:\n1. Order\n2. Cars\n3. Client\n4. Calculator\nq. Exit program")
        choice = input("> Choose a section: ")
        if choice == "1":
            order_UserInterface = Order_UI()
            order_UserInterface.order_menu()
        elif choice == "2":
            car_UserInterface = Car_UI()
            car_UserInterface.car_menu()
        elif choice == "3":
            client_UserInterface = Client_ui()
            client_UserInterface.main_menu()
        elif choice == "4":
            calc_UserInterface = Calc_UI()
            calc_UserInterface.calc_menu()      
        elif choice == "q":
            print("Exiting program...")
            break
        else:
            print("Invalid input!")      
                        
main()
