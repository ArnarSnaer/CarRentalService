class Insurance(object):
    def __init__(self, ins_type):
        self.ins_type = ins_type
        self.price = 0

        if self.ins_type == "t1":
            self.price = 10000
        elif self.ins_type == "t2":
             self.price = 20000
        elif self.ins_type == "t3":
             self.price = 5000
    
    def __str__(self):
        return "{}".format(self.price)

    def __radd__(self,other):
        return int(self.price + other)

tala = Insurance("t1")
print(tala)