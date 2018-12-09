from client import Client

class ClientRepo():
    def __init__(self):
        self.info = []

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
        # for item in self.info

    ''' þetta forrit gefur Client object is not iterable    
    for item in client:
                print(item)
                to_write = str(item)
                open_file.write(to_write)
                if item != self.info[-1]:
                    open_file.write(",")

            open_file.write("\n")

            open_file.close()'''

    def remove_customer(self):
        '''vantar að gera input setningarnar flottari, vantar að villu-checka'''
        client_found = False
        searchword = input("Input a phone-number, address, license-number or etc.\n")

        open_file = open("clist.txt", "r")
        lines = open_file.readlines()
        open_file.close()

        open_file = open("clist.txt", "w")
        for line in lines:
            if searchword not in line:
                open_file.write(line)
            elif searchword in line:
                client_found = True
        if client_found:
            print("Client found, removing client")
        else:
            print("Client not found")

        open_file.close()

    def find_client(self,searchword):
        # searchword = input("Input a phone-number, address, license-number or etc.\n")
        ''' Hér vantar villu-check -->'''
        open_file = open("clist.txt", "r")
        client_found = False
        for line in open_file:
            if searchword in line:
                client_found = True
                found_list = line.split(",")
                # print(found_list)
        if client_found: 
            return found_list
        else:
            return "Client not found"

# mysearch = ClientRepo().new_customer()
# Jann Kounias,Seahaven 176,546-799-42066,17. Oktober,4011148563,USA,159
