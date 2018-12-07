from func_print_GUI import print_GUI
from func_user_input import user_input
from func_shutting_down import shutting_down
from func_lookup_client import lookup_client

go_again = True

while go_again:
    print_GUI()
    choice = user_input()

    if choice == "3":
        lookup_client()

    if choice == "0":
        shutting_down()
        go_again = False