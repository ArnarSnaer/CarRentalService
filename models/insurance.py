class Insurance(object):
    def __init__(self, type):
        self.type = type
        self.price = 0

        if self.type == "t1":
            self.price = 10000
        elif self.type == "t2":
             self.price = 20000
        elif self.type == "t3":
             self.price = 5000
    
    def __str__(self):
        return "{}".format(self.price)

tala = Insurance("t1")
print(tala)