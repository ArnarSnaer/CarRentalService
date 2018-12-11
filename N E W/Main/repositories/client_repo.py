from models.client_model import Client

class ClientRepo():
    def __init__(self):
        self.info = []

    def new_customer(self):
        open_file = open("./data/clients.txt", "a")

        for item in self.info:
            to_write = str(item)
            open_file.write(to_write)
            if item != self.info[-1]:
                open_file.write(",")

        open_file.write("\n")

        open_file.close()

    def remove_customer(self, name):
        open_file = open("./data/clients.txt", "r")
        old_file = open_file.readlines()
        open_file.close()

        new_file = open("./data/clients.txt", "w")
        for line in old_file:
            if name not in line:
                new_file.write(line)

        new_file.close()

    def find_client(self, searchword):
        open_file = open("./data/clients.txt", "r")

        for line in open_file:
            if searchword in line:
                found_list = line.split()
                print(found_list)
    
        return found_list