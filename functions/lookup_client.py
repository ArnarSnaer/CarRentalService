from functions.models.client import Client
from functions.lookup_client_prompt import lookup_client_prompt

def lookup_client():
    with open("clients.txt", "r") as text_file:
        info = lookup_client_prompt()
        for line in text_file:
            info_list = line.split(",")

            if info in info_list:
                chosen_client = Client(info_list[0],info_list[1],info_list[2],info_list[3],info_list[4],info_list[5],info_list[6],)
                print(chosen_client)