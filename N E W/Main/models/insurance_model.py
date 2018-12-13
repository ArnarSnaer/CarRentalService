class Insurance(object):
    def __init__(self, ins_type=""):
        self.ins_type = ins_type
        self.price = 0
        self.title_list = ["Water damage insurance","CASCO insurance","Theft insurance","Collision damage insurance"]
        self.price_list = [12000,10000,20000,5000]

        if self.ins_type == "base":
            self.price = self.price_list[0]
        elif self.ins_type == "t1":
            self.price = self.price_list[1]
        elif self.ins_type == "t2":
             self.price = self.price_list[2]
        elif self.ins_type == "t3":
             self.price = self.price_list[3]
    
    def __str__(self):
        return "{}".format(int(self.price))
    
    def __radd__(self,other):
        return int(self.price + other)

    def get_price(self):
        return self.price
    
    def get_price_list(self):
        return self.price_list
    
    def get_title_list(self):
        return self.title_list

#tala = Insurance("t1")
#print(tala)
# __radd__ er add fyrir tvær gerðir af mismunandi gerðum