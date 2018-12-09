from my_client_repo import ClientRepo
from client import Client

class Client_ser(object):
    def __init__(self):
        self.__client = ClientRepo()
    
    def update_registration(self, __client):
        print("What would you like to update?\n1. Name\n2. Address\n3. Phone number\n4. Birthday\n5. Drivers license number\n6. Country\n7. Zip")
        
        choice = int(input("Please input the integer of your choice: "))
        change = input("New info is: ")
        # # Setja villucheck seinna ef einvher reynir að skrifa inn nafnið á upplýsingarreitinum
        # self.info[choice-1] = change
        # return self.info
    
    def get_client(self):
        self.searchword = input("Input a phone-number, address, license-number or etc.\n")
        results = self.__client.find_client(self.searchword)

        # return "Name: {}\nAddress: {}\nPhone number: {}\nBirthday: {}\nDrivers license number: 
        # {}\nCountry: {}\nZip: {}".format(self.name,self.address,self.phone,self.birthday,self.driver_num, self.country,self.zip)

        print(results)

    def new_client(self, client):
        self.__client.new_client(client)

    def make_change(self):
        pass
        #Ehvs

''' finnst mér að ætti að vera í UI en ekki í servicees og mun ég færa það yfir í UI þegar við fáum allt heila dæmið til að virka'''
fullname = input("Fullname: ")
address = input("Adress: ")
phonenumber = input("Phone number: ")
'''villu-check needed'''
birthday = input("date of birth: ")
licensenumber = input("License number: ") 
country = input("Country(using Alpah-3 order): ")
the_zip = input("Zip: ")
new_client = Client(fullname, address, phonenumber, birthday, licensenumber, country, the_zip)
mytry = Client_ser().new_client(new_client)
'''Marcy Swett,Litenway 170,555-632-20937,0. November,9281318350,Isl,928'''