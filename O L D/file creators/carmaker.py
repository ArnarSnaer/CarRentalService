import random
import string
def create_plate():
    string.letters = 'ABCDEFGHIJKLMNOPQRSTUWYZ'
    first = random.choice(string.letters)
    second = random.choice(string.letters)
    fourth = str(random.randint(0,9))
    fifth = str(random.randint(0,9))
    case = random.randint(0,1)
    
    if case == 1:
        third =str(random.randint(0,9)) 
    else:
        third = random.choice(string.letters)
    the_plate= first+second+third+fourth+fifth
    # print(the_plate)
    return the_plate

def random_car():
    the_brands =["Toyota", "Alfa Romeo", "Campagna", 'Saturn', 'Chevrolet', 'Suzuki',
                   'Marcos', 'Unique', 'Bentley', 'LandRover','Ferrari', 'Lincoln', 'Audi']
    the_types = ['Hatchback', 'Sedan', 'MPV', 'SUV', 'Crossover', 'Coupe', 'Convertible', 'Sport']
    brand_rand = random.randint(0,len(the_brands)-1)
    type_rand = random.randint(0,len(the_types)-1)

    my_brand = the_brands[brand_rand]
    my_type = the_types[type_rand]
    # print[my_type, my_brand]
    return [my_type, my_brand]

def drive():
    drives = ["4WD", "FWD", "RWD"]
    num = random.randint(0,len(drives)-1)
    return drives[num]

def is_avail():
    num = random.randint(0,1)
    state = True
    if num == 0:
        state = False
    return state        

def Manual():
    myGears = ["MANUAL", "AUTO"]
    num = random.randint(0,1)
    return myGears[num] 
    
def length():
    return random.randint(500, 100000)

''' records def mögulegt'''
def fuel():
    fuels = ["GAZOLINE", "DIESEL"]
    return fuels[random.randint(0,1)]

def price():
    priced = random.randint(2,20)*12000
    return priced

def vehicle():
    with open("vehicle.txt", "w") as my_text:
        list_of_plates = []
        for i in range(300):
            my_plate = create_plate()
            if my_plate not in list_of_plates:
                my_car = random_car()
                final = "{},{},{},{},{},{},{},{},{}".format(my_car[0],my_car[1], my_plate, drive(), is_avail(), Manual(), length(), fuel(), price() )
                # print(final)
                my_text.write(final)
                my_text.write("\n")
            list_of_plates.append(my_plate)

vehicle()
# create_plate()
# random_car()


