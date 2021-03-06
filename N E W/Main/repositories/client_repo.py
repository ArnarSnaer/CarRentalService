from models.client_model import Client
# from models.client_model import Client
import string

class ClientRepo():
    def __init__(self):
        
        
        self.NAME = 0
        self.ADDRESS = 1
        self.PHONE = 2
        self.BIRTHDAY = 3
        self.LICENSE_NUM = 4
        self.COUNTRY = 5
        self.THE_ZIP = 6
        
    def new_client(self, client):
        ''' This function writes in the new client if the client does not already exist'''
        open_file = open("./data/clients.txt", "a+")
        fullname = client.get_name()
        address = client.get_address()
        phone = client.get_phone()
        phone = self.int_format(phone)
        birthday = client.get_birthday()
        license_num = client.get_license_num()
        country = client.get_country()
        the_zip = client.get_zip()

        open_file.write("{},{},{},{},{},{},{}".format(fullname, address, phone, birthday, license_num, country, the_zip))
        open_file.write("\n")
        open_file.close()
       
    def remove_client(self, searchword):
        '''This function removes the client from the database'''

        open_file = open("./data/clients.txt", "r")
        lines = open_file.readlines()
        open_file.close()
        client_found = False
        
        open_file = open("./data/clients.txt", "w")
        for line in lines:
            if searchword not in line:
                open_file.write(line)
            elif searchword in line:
                client_found = True
        open_file.close()
        return client_found
        

    def find_client(self,searchword):
        ''' This function returns the client's info if he is registered in the database'''
        open_file = open("./data/clients.txt", "r")
        client_found = False
        for line in open_file:
            if searchword in line:
                client_found = True
                client_list = line.split(",")
        if client_found: 
            return client_list
        else:
            return False

    def update_registration(self, client_info, option, the_change):
        '''This function takes in a client's info and where and what the change should be'''
        client_update = self.change_element(client_info, option, the_change)
        open_file = open("./data/clients.txt", "a+")
        client_update_list = client_update
        client_update = Client(client_update[self.NAME], client_update[self.ADDRESS], client_update[self.PHONE], client_update[self.BIRTHDAY], client_update[self.LICENSE_NUM],
                                    client_update[self.COUNTRY], client_update[self.THE_ZIP])
        self.new_client(client_update)
        open_file.close()
        return client_update_list
     


    def change_element(self, the_client, update_choice, the_change):
        '''searches in a list and changes a selected value and returns the list'''
        
        the_client[update_choice -1] = the_change
        
        return the_client

    def int_format(self, phone):
        '''Creates a special format for phone-number'''
        my_phone = phone
        my_phone = list(my_phone)
        if "-" not in my_phone:
        
            result_str = ""
            my_phone_len = len(my_phone) 
            
            while my_phone_len > 6:
                for i in range(3):
                    result_str += my_phone.pop(0)
                result_str += "-"
                my_phone_len -= 3
            end_str = ''.join(my_phone)
            result_str += end_str
            return result_str
        return ''.join(my_phone)
