from repositories.client_repo import ClientRepo
# from repositories.client_repo import ClientRepo
# from client import Client
import string


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
        # self.INFO = 7
        self.PHONELENGTH_MIN = 7
        self.LICENSE_LENGTH = 10
    
    def update_registration(self, searchword, option, the_change):
        updated = False
        invalidate =''
        updated_client = []
        client_info, client_found = self.get_client(searchword)
        if client_found == True and type(client_info)==list:                
                client_update = self.__client_repo.change_element(client_info, option, the_change)
                valid, invalidation = self.is_valid_client(client_update)
                if valid:
                    self.__client_repo.remove_client(searchword)
                    # spurninga að taka þetta if statement
                    updated_client = self.__client_repo.update_registration(client_info, option, the_change)
                    updated = True
                else:
                    invalidate = invalidation

                
        return updated, invalidate, updated_client
    
    def get_client(self, searchword):
        client_info = self.__client_repo.find_client(searchword)
        client_found = True
        if client_info == False:
            client_found = False
        return client_info, client_found

    def new_client(self, client):
        valid, invalidation = self.is_valid_client(client)
        if valid:
            self.__client_repo.new_client(client)
            return valid, invalidation
        else:
            return valid, invalidation

    def remove_client(self, searchword):
        '''spurning um að sleppa client_found og nota bara self.client.remove.... til að skila True'''
        client_found = False
        if self.__client_repo.remove_client(searchword):
            client_found = True
        return client_found

    def is_valid_client(self, client):
        clients_info = []
        if type(client) != list:
            for attr, value in client.__dict__.items():
                clients_info.append(value)
        else:
             for element in client:
                clients_info.append(element)
        
        valid, invalidation = self.check_input(clients_info)
        return valid, invalidation



    def check_input(self, clients_info):
        valid = False
        invalidation ='' 

        if not self.check_if_letters(clients_info[self.NAME]):
            invalidation = "A name can only contain alpahabetical letters"
            return valid, invalidation
        
        validation, counter = self.check_if_integers(clients_info[self.PHONE])
        if (validation == False or counter < 7):
            invalidation = "Ivalid phone number"
            return valid, invalidation
            
        validation, counter = self.check_if_integers(clients_info[self.LICENSE_NUM])
        if (validation == False or counter != 10) or not validation:
            invalidation = "Invalid license number, license number must contain 10 integers from 0-9"
            return valid, invalidation

        if not self.check_if_letters(clients_info[self.COUNTRY]):
            invalidation = "A country's Alpha 3 can only contain letters"
            return valid, invalidation            
        
        validation, counter = self.check_if_integers(clients_info[self.THE_ZIP])
        if (validation == False, counter !=3) :
            invalidation = "A zip code can only contain integers not letters"
            return valid, invalidation
        else:
            valid = True
        
        return valid , invalidation
        
        
       
    def check_if_letters(self, variable):
        validation = False
        int_count = 0
        letter_count = 0
        for letter in variable:
            if letter.isdigit():
                int_count += 1
            if letter.isalpha():
                letter_count +=1
                
        if (int_count == 0 and letter_count > 0):
            validation = True
            return validation
        else:
            return validation



    def check_if_integers(self, variable):
        validation = False
        try:
            counter = 0
            variable = list(variable)
            for integer in variable:
                if integer != "-" and integer != "\n" : 
                    int(integer)
                    counter += 1
            validation = True
            return validation , counter
        except ValueError:
            counter = 0                     #PRUFA AÐ HAFA COUNTER MEÐ EN AÐ HAFA HANN 0
            return validation , counter
 
    # def check_if_contain_int_and_str(self, variable):
    #     for i in



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