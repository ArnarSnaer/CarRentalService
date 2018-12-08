from 

class Client_ser(object):
    def __init__(self):
        #Ehv
    
    def update_registration(self):
        print("What would you like to update?\n1. Name\n2. Address\n3. Phone number\n4. Birthday\n5. Drivers license number\n6. Country\n7. Zip")
        
        choice = int(input("Pleaes input the integer of your choice: "))
        change = input("New info is: ")
        # Setja villucheck seinna ef einvher reynir að skrifa inn nafnið á upplýsingarreitinum
        self.info[choice-1] = change
        return self.info
    
    def get_client(self):
        return "Name: {}\nAddress: {}\nPhone number: {}\nBirthday: {}\nDrivers license number: {}\nCountry: {}\nZip: {}".format(self.name,self.address,self.phone,self.birthday,self.driver_num, self.country,self.zip)
    
    def make_change(self):
        #Ehvs
    
