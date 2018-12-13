<<<<<<< HEAD
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
=======
str_1 = "t"
str_2 = str_1.split(" ")

print(str_2)
>>>>>>> 945686592a7e20dae196338ec75d30fcb34d6e8e
