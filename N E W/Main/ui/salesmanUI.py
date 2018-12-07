from UI.print_GUI import print_GUI
from UI.user_input import user_input
from UI.shutting_down import shutting_down
from UI.lookup_client import lookup_client
from UI.redirect_user import redirect_user

class salesmanUI():
    go_again = True

    while go_again:
        print_GUI()
        choice = user_input()

        if choice == "0":
            shutting_down()
            go_again = False
        else:
            redirect_user(choice)