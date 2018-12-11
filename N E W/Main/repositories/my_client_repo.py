from models.client_model import Client
import string
'''vantar að breyta nafni txt skjala'''
'''villucheck fyrir alla liði'''

class ClientRepo():
    def __init__(self):
        # self.info = []
        
        self.NAME = 0
        self.ADDRESS = 1
        self.PHONE = 2
        self.BIRTHDAY = 3
        self.LICENSE_NUM = 4
        self.COUNTRY = 5
        self.THE_ZIP = 6
        self.INFO = 7
    
    def new_client(self, client):
        ''' þarf að implementa að það geti ekki verið hægt að bæta við einstakling sem er núþegar í listanum'''
        open_file = open("clist.txt", "a+")
        fullname = client.get_name()
        address = client.get_address()
        phone = client.get_phone()
        birthday = client.get_birthday()
        license_num = client.get_license_num()
        country = client.get_country()
        the_zip = client.get_zip()

        open_file.write("{},{},{},{},{},{},{}".format(fullname, address, phone, birthday, license_num, country, the_zip))
        open_file.write("\n")
        open_file.close()
       
    def remove_client(self, searchword):
        '''vantar að villu-checka'''
        # client_found = False

        open_file = open("clist.txt", "r")
        lines = open_file.readlines()
        open_file.close()

        open_file = open("clist.txt", "w")
        for line in lines:
            if searchword not in line:
                open_file.write(line)
            elif searchword in line:
                client_found = True
        open_file.close()
        return client_found
        

    def find_client(self,searchword):
        # searchword = input("Input a phone-number, address, license-number or etc.\n")
        ''' Hér vantar villu-check -->'''
        open_file = open("clist.txt", "r")
        client_found = False
        for line in open_file:
            if searchword in line:
                client_found = True
                client_list = line.split(",")
                # print(found_list)
        if client_found: 
            return client_list
        else:
            return False

    def update_registration(self, client_info, option):
<<<<<<< HEAD
        # open_file = open("clist.txt", "r")
        # the_client = ClientRepo().find_client(searchword)
        #client_found = False
        if type(client_info) == list:
        #    client_found = True
            # print("Client found")
            # while True:
            client_update = self.get_from_list(client_info, option)
            # self.remove_client(client_info)
            open_file = open("clist.txt", "a+")
            client_update = Client(client_update[self.NAME], client_update[self.ADDRESS], client_update[self.PHONE], client_update[self.BIRTHDAY], client_update[self.LICENSE_NUM],
                                        client_update[self.COUNTRY], client_update[self.THE_ZIP])
            self.new_client(client_update)
            open_file.close()
            print("Update complete!")

        else:
            print("Client not found")
=======
        updated = False
        # if type(client_info) == list:
        client_update = self.change_element(client_info, option)
        open_file = open("clist.txt", "a+")
        client_update = Client(client_update[self.NAME], client_update[self.ADDRESS], client_update[self.PHONE], client_update[self.BIRTHDAY], client_update[self.LICENSE_NUM],
                                    client_update[self.COUNTRY], client_update[self.THE_ZIP])
        self.new_client(client_update)
        open_file.close()
        updated = True
        return updated
>>>>>>> 4170a64e484d72f540f19a95d19bc2234f86250a


    def change_element(self, the_client, update_choice):
        '''searches in a list and changes a selected value and returns the list'''
        
        the_change = input("Insert new info: ")

        '''vantar villu-check'''
        the_client[update_choice -1] = the_change
        
        return the_client


# mysearch = ClientRepo().new_customer()
# Jann Kounias,Seahaven 176,546-799-42066,17. Oktober,4011148563,USA,159
