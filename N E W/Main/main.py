from ui.calc_ui import Calc_UI
from ui.car_ui import Car_UI
from ui.order_ui import Order_UI
from ui.client_ui import Client_ui
from models.order_model import Order
import os

def main():
    print("Welcome, User\n","-"*86)
    choice = ""
    # CR147,2019-06-21,2019-06-28,WS608,Xefu,123456789,Gunnar,228000
    while choice != "q" or choice!= "Q": 
        os.system('cls')
        print("Available sections:\n1. Order\n2. Cars\n3. Client\n4. Calculator\nq. Exit program")
        choice = input("> Choose a section: ")
<<<<<<< HEAD
        if (choice == "1") or (choice == "Order"):
            order_UserInterface = Order_UI()
            order_UserInterface.order_menu()
        elif (choice == "2") or (choice == "Cars"):
            car_UserInterface = Car_UI()
            car_UserInterface.car_menu()
        elif (choice == "3") or (choice == "Client"):
            client_UserInterface = Client_ui()
            client_UserInterface.main_menu()
        elif (choice == "4") or (choice == "Calculator"):
            calc_UserInterface = Calc_UI()
            calc_UserInterface.calc_menu()
        elif (choice == "q") or (choice == "Q"):
            print("Exiting program...\n")
=======
        if choice == "1":
            os.system('cls')
            order_UserInterface = Order_UI()
            order_UserInterface.order_menu()
        elif choice == "2":
            os.system('cls')
            car_UserInterface = Car_UI()
            car_UserInterface.car_menu()
        elif choice == "3":
            os.system('cls')
            client_UserInterface = Client_ui()
            client_UserInterface.main_menu()
        elif choice == "4":
            os.system('cls')
            calc_UserInterface = Calc_UI()
            calc_UserInterface.calc_menu()      
        elif choice =="q" or choice=="Q":
            print("-"*86,"\nExiting program...\n")
>>>>>>> a9603752a19f47ba9ed2bc408e183decfb937c22
            break
        else:
            print("Invalid input!")   
                        
main()