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

    def get_name(self):
        return "{}".format(self.info[0])

    def update_registration(self):
        print("What would you like to update? (Please input integer choice)")
        print("1. Name\n2. Address\n3. Phone number\n4. Birthday\n5. Drivers license number\n6.Country\n7. Zip")
        
        choice = int(input(""))
        change = input("New info is: ")
        
        self.info[choice-1] = change
        return self.info

    def new_customer(self):
        open_file = open("clients.txt", "a")

        for item in self.info:
            to_write = str(item)
            open_file.write(to_write)
            if item != self.info[-1]:
                open_file.write(",")

        open_file.write("\n")

        open_file.close()

    def remove_customer(name):
        open_file = open("clients.txt", "r")
        old_file = open_file.readlines()
        open_file.close()

        new_file = open("clients.txt", "w")
        for line in old_file:
            if name not in line:
                new_file.write(line)

        new_file.close()

    def __str__(self):
        return str(self.info)
    
    def __getitem__(self,index_num):
        return self.info[index_num]
    
    def __iter__(self):
        return iter(self.info)
    
vinur = Client("John", "Geysir 7", 5885522,"17 June", "1234 5678", "USA", "779")

vinur.update_registration()
vinur.get_client
vinur.new_customer()
rude_guy = input("Enter name of person you want to remove from list: ")
Client.remove_customer(rude_guy)
