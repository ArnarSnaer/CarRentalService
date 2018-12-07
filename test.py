import random
def birthday():
    num_1 = random.randint(0,2)
    if num_1 == 0:
        num_2 = 1
        date = random.randint(0,29)
    elif num_1 == 1:
        num_2 = random.randint(0,2)
        date = random.randint(0,30)
    elif num_1 == 2:
        num_2 = random.randint(0,7)
        date = random.randint(0,31)

    print(num_1)
    print(num_2)
    print(date)

    months = [["Febuary"],["April","September","November"],["January","March","May","June","July","August","Oktober","December"]]
    chosen_month = months[num_1][num_2]
    print(chosen_month)
    b_day = str(date) + ". " + chosen_month
    return b_day

print(birthday())



