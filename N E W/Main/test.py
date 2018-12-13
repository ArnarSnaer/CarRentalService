def check_if_integers(self, variable):
    try:
        variable = list(variable)
        for integer in variable:
            if integer != "-" or integer != "\n" : 
                int(integer)
        return True
    except ValueError:
        return False

print("-" in "546-799-59010")

variable = list("546-799-59010\n")
for integer in variable:
    if integer != "-" and integer != "\n" : 
        print(integer)
