from functions.print_GUI import print_GUI
from functions.user_input import user_input
from functions.shutting_down import shutting_down
from functions.lookup_client import lookup_client
from functions.redirect_user import redirect_user


go_again = True

while go_again:
    print_GUI()
    choice = user_input()

    if choice == "0":
        shutting_down()
        go_again = False
    else:
        redirect_user(choice)