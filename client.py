class Client(object):
    def __init__(self,name,address,phone,birthday,driver_num,country,zip):
        self.name = name
        self.address = address
        self.phone = phone
        self.birthday = birthday
        self.driver_num = driver_num
        self.country = country
        self.zip = zip
        self.info = [self.name, self.address,self.phone,self.birthday,self.driver_num,self.country,self.zip]
    
    def get_client(self):
        return "Name: {}\nAddress: {}\nPhone number: {}\nBirthday: {}\nDrivers license number: {}\nCountry: {}\nZip: {}".format(self.name,self.address,self.phone,self.birthday,self.driver_num, self.country,self.zip)

    def update_registration(self):
        print("What would you like to update?")
        print("1. Name\n2. Address\n3. Phone number\n4. Birthday\n5. Drivers license number\n6.Country\n7. Zip")
        
        choice = int(input(""))
        change = input("New info is: ")
        
        self.info[choice-1] = change
        return self.info

    def __str__(self):
        return str(self.info)
    
    def __getitem__(self,index):
        return self.info[index]
    
    def __iter__(self):
        return iter(self.info)
    
# vinur = Client("Jón", "Geysir 7", 5885522,"17 Júní", "1234 5678", "USA", "779")

# print(vinur.get_client())
# vinur.update_registration()
# print(vinur)