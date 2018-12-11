from services.payment_service import Payment_ser

class Payment_UI(object):
    def __init__(self):
        self.payment_service = Payment_ser

    def payment_menu(self):
        choice = ""
        while choice != "q":
            print("Current section:\n1. Add insurance\n2. Remove insurance\n3. Print insurance prices\nq. Quit")
            choice = ("> What would you like to do? enter 'q' to quit.")
        
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "q":
                pass
            else:
                pass