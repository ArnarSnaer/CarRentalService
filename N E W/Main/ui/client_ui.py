# from services.client_services import Client_ser
# from models.client_model import Client
from client_services import Client_ser
from client import Client
import string
'''þetta UI hefur back option, hægt að hafa það með eða eyða því'''

class Client_ui():
    def __init__(self):
        self.__client_ser = Client_ser()
    
        self.NAME = 0
        self.ADDRESS = 1
        self.PHONE = 2
        self.BIRTHDAY = 3
        self.LICENSE_NUM = 4
        self.COUNTRY = 5
        self.THE_ZIP = 6
        self.INFO = 7
        

    def main_menu(self):
        stay = True
        while stay:
            print("1. Create a new client\n2. See client full imformation\n3. Remove a client\n4. Update client's information\n5. Back")
            option = input("> Input an option: ")
            the_range = range(1,6)
            if option == "5" :
                stay = False
            else:
                if self.check_option(option, the_range):
                    self.client_op(option)
                else:
                    print("Please input an integer from 1 to 5")
    
    def check_option(self, option, the_range):
            try: 
                option = int(option)
                if option in the_range:
                    return True
            except ValueError:
                return False

    def client_op(self, option):
        if option == "1":
           self.option_1()
        else:
            print("Input a searchword, using a clients license number or phone number is recommended ")
            searchword = input("> Searchword: ")
            if option == "2":
                self.option_2(searchword)
            elif option == "3":
                self.option_3(searchword)
            elif option == "4":
                self.option_4(searchword)
            elif option == "5":
                return option
    
    def option_1(self):
        fullname = input("> Fullname: ")
        address = input("> Address: ")
        phone_number = input("> Phone number: ")
        '''villu-check needed'''
        birthday = input("> Date of birth: ")
        license_number = input("> License number: ") 
        country = input("> Country(using Alpah-3 order): ")
        the_zip = input("> Zip: ")
        '''check if client already exists'''
        '''nobody has the same license number'''
        
        info_list, client_found = self.check_if_already_client(license_number)
        if not client_found:
            new_client = Client(fullname, address, phone_number, birthday, license_number, country, the_zip)
            self.__client_ser.new_client(new_client)
            info_list = [fullname, address, phone_number, birthday, license_number, country, the_zip]
            print(info_list)
        return info_list

    def check_if_already_client(self, license_number):
        info_list, client_found = self.__client_ser.get_client(license_number)
        if client_found:
            print("Client already exists")
            print(self.my_list_format(info_list))
        return info_list, client_found
            
    def option_2(self, searchword):
        info_list, client_found = self.__client_ser.get_client(searchword)
        if client_found:
            print(self.my_list_format(info_list))
            return info_list
        else:
            print("Client not found")

    def option_3(self, searchword):
        if self.option_2(searchword):
            if self.__client_ser.remove_client(searchword):
                print("Client found, removing client")
            
    def option_4(self, searchword):
        client_info, client_found = self.__client_ser.get_client(searchword)
        if client_found:
            stay = True
            while stay:
                the_range = range(1,9)
                option = self.option_4_main_menu()
                if option == "8":
                    stay = False
                else:
                    if self.check_option(option, the_range):
                        if self.__client_ser.update_registration(searchword, int(option)):
                            print("Updated")
                    else: 
                        print("Please input an integer from 1 to 8")
        else: 
            print("Client not found")

    def option_4_main_menu(self):
        print("What would you like to update?\n1. Name\n2. Address\n3. Phone number\n4. Birthday\n5. Drivers license number\n6. Country\n7. Zip\n8. Quit")
        option = input("> Input an option: ")
        return option
    
    def my_list_format(self, a_list):
        return "Clients info as follows: \nName: {}\nAddress: {}\nPhone number: {}\nDate of birth: {}\nLicense number: {}\nCountry: {}\nZip: {}".format(a_list[self.NAME],
                                        a_list[self.ADDRESS], a_list[self.PHONE], a_list[self.BIRTHDAY], a_list[self.LICENSE_NUM], a_list[self.COUNTRY], a_list[self.THE_ZIP])

    def order_menu(self):
        clients_info = ""
        print("Is the client already registered?  y/n: ") 
        while clients_info == "":
            answer = input("> ")
            answer = answer.lower() 
            if answer == "n":
                clients_info = self.client_op("1")
            elif answer == "y":
                clients_info = self.client_op("2")
            else:
                print("Please input either the letter 'y' or the letter 'n'")




Client_ui().order_menu()