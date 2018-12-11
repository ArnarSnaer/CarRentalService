from my_client_repo import ClientRepo
# from client import Client

class Client_ser(object):
    def __init__(self):
        self.__client_repo = ClientRepo()

        self.NAME = 0
        self.ADDRESS = 1
        self.PHONE = 2
        self.BIRTHDAY = 3
        self.LICENSE_NUM = 4
        self.COUNTRY = 5
        self.THE_ZIP = 6
        self.INFO = 7
    
    def update_registration(self, searchword, option):
        updated = False
        client_info, client_found = self.get_client(searchword)
        if client_found == True and type(client_info)==list:
                self.__client_repo.remove_client(searchword)
                if self.__client_repo.update_registration(client_info, option):
                    updated = True
        return updated
    
    def get_client(self, searchword):
        client_info = self.__client_repo.find_client(searchword)
        client_found = True
        if client_info == False:
            client_found = False
        return client_info, client_found

    def new_client(self, client):
        if self.is_valid_client(client):
            self.__client_repo.new_client(client)

    def remove_client(self, searchword):
        '''spurning um að sleppa client_found og nota bara self.client.remove.... til að skila True'''
        client_found = False
        if self.__client_repo.remove_client(searchword):
            client_found = True
        return client_found

    def is_valid_client(self, client):
        clients_info = []
        for attr, value in client.__dict__.items():
            clients_info.append(value) 

        '''try except föll nauðsynleg'''
        
        return True
        



# ''' finnst mér að ætti að vera í UI en ekki í servicees og mun ég færa það yfir í UI þegar við fáum allt heila dæmið til að virka'''
# fullname = input("Fullname: ")
# address = input("Adress: ")
# phonenumber = input("Phone number: ")
# '''villu-check needed'''
# birthday = input("date of birth: ")
# licensenumber = input("License number: ") 
# country = input("Country(using Alpah-3 order): ")
# the_zip = input("Zip: ")
# new_client = Client(fullname, address, phonenumber, birthday, licensenumber, country, the_zip)
# mytry = Client_ser().new_client(new_client)
# '''Marcy Swett,Litenway 170,555-632-20937,0. November,9281318350,Isl,928'''


# '''prófa remove_client'''
# searchword = input("Input a phone-number, address, license-number or etc.\n")
# Client_ser().remove_client(searchword)


# '''prófa update registration'''
# searchword = input("Input a phone-number, address, license-number or etc.\n")
# Client_ser().update_registration(searchword)