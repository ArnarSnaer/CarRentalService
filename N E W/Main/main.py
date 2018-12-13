from ui.calc_ui import Calc_UI
from ui.car_ui import Car_UI
from ui.order_ui import Order_UI
from ui.client_ui import Client_ui
from models.order_model import Order

def main():
    print("Welcome, User")
    choice = ""
    # CR147,2019-06-21,2019-06-28,WS608,Xefu,123456789,Gunnar,228000
    while choice != "q" or choice!= "Q": 
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
        elif choice =="q" or choice=="Q":
            print("Exiting program...")
            break
        else:
            print("Invalid input!")      
                        
main()
