class Client(object):
    def __init__(self,name,address,phone,birthday,license_num,country,the_zip):
        self.name = name
        self.address = address
        self.phone = phone
        self.birthday = birthday
        self.license_num = license_num
        self.country = country
        self.the_zip = the_zip
        self.info = [self.name, self.address, self.phone, self.birthday, self.license_num, self.country, self.the_zip]

    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.name, self.address, self.phone, self.birthday, self.license_num, self.country, self.the_zip)
    
    def __repr__(self):
        return self.__str__()

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_birthday(self):
        return self.birthday

    def get_license_num(self):
        return self.license_num

    def get_country(self):
        return self.country

    def get_zip(self):
        return self.the_zip