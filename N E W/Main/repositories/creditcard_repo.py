from models.creditcard import Creditcard

class CreditcardRepo():
    def __init__(self):
        self.info = []

    def add_creditcard(self):
        open_file = open("./data/creditcard.txt", "a")

        for item in self.info:
            to_write = str(item)
            open_file.write(to_write)
            if item != self.info[-1]:
                open_file.write(",")

        open_file.write("\n")

        open_file.close()

    def remove_creditcard(self, plate):
        open_file = open("./data/creditcard.txt", "r")
        old_file = open_file.readlines()
        open_file.close()

        new_file = open("./data/creditcard.txt", "w")
        for line in old_file:
            if plate not in line:
                new_file.write(line)

        new_file.close()

    def find_card(self, searchword):
        open_file = open("./data/creditcard.txt", "r")
        
        for line in open_file:
            if searchword in line:
                found_list = line.split()
                print(found_list)