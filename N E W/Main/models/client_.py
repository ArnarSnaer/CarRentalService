class Client(object):
    def __init__(self,name,address,phone,birthday,license_num,country,the_zip):
        self.name = name
        self.address = address
        self.phone = phone
        self.birthday = birthday
        self.license_num = license_num
        self.country = country
<<<<<<< HEAD
        self.the_zip = the_zip
        self.info = [self.name, self.address, self.phone, self.birthday, self.license_num, self.country, self.the_zip]
=======
        self.zip = zip
        self.info = [self.name, self.address, self.phone, self.birthday, self.driver_num, self.country, self.zip]
<<<<<<< HEAD
=======
>>>>>>> 6435afc58e4e266871ded234d09d0d644ab7df93

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
>>>>>>> a49268ecc52f7e37c72758ca8f41b711e53f46e1

    def get_license_num(self):
        return self.license_num

    def get_country(self):
        return self.country

    def get_zip(self):
        return self.the_zip
