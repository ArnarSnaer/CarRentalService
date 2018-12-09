class Client(object):
    def __init__(self,name,address,phone,birthday,driver_num,country,zip):
        self.name = name
        self.address = address
        self.phone = phone
        self.birthday = birthday
        self.driver_num = driver_num
        self.country = country
        self.zip = zip
        self.info = [self.name, self.address, self.phone, self.birthday, self.driver_num, self.country, self.zip]

    def __str__(self):
        return str(self.info)
    
    def __getitem__(self,index):
        return self.info[index]
    
    def __iter__(self):
        return iter(self.info)

'''
vinur = Client("John", "Geysir 7", 5885522,"17 June", "1234 5678", "USA", "779")

vinur.update_registration()
vinur.get_client
vinur.new_customer()
rude_guy = input("Enter name of person you want to remove from list: ")
Client.remove_customer(rude_guy)
'''