from repositories.client_repo import ClientRepo
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
        self.PHONELENGTH_MIN = 7
        self.LICENSE_LENGTH = 10
    
    def update_registration(self, searchword, option, the_change):
        '''Here is where the update of client's info goes through
           If the input for the update is not valid then the code will return a invalidation-string'''
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
        '''Gets client info if the client exists'''
        client_info = self.__client_repo.find_client(searchword)
        client_found = True
        if client_info == False:
            client_found = False
        return client_info, client_found

    def new_client(self, client):
        '''Creates new client'''
        valid, invalidation = self.is_valid_client(client)
        if valid:
            self.__client_repo.new_client(client)
            return valid, invalidation
        else:
            return valid, invalidation

    def remove_client(self, searchword):
        '''Removes client if found in the database'''
        client_found = False
        if self.__client_repo.remove_client(searchword):
            client_found = True
        return client_found

    def is_valid_client(self, client):
        '''Checks if the client has valid information, it can take both 
        instances of client and a list containing a client's info'''
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
        '''Checks if all the info the client has are valid, all phone-numbers must have 7 digits or more and license-numbers must contain 10 digits
            If any of the client's information are not valid then this function returns an invalidation statement '''
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
        if (validation == False or counter !=3) :
            invalidation = "A zip code can only contain integers not letters"
            return valid, invalidation
        else:
            valid = True
        
        return valid , invalidation
           
       
    def check_if_letters(self, variable):
        ''' Checks if the variable contains only letters'''
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
        '''Checks if a variable contains only integers and returns how many they are'''
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
            counter = 0                     
            return validation , counter
