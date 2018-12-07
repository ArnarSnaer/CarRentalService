import random
import string

def firstname():
    list_of_names = ["Gonzalo", "Janita","Lawrence","Thelma","Miyoko","Reiko","Bell","Meredith","Phillip","Kandis",
                        "Dominick","Marianela","Deidre","Dorcas","Josette","Corrine","Shan","Vernita","Marquis","Alverta","Leonarda","Gary","Jann","Han","Jutta","Delilah","Cortney","Marcy","Teena","Darrin"]
    num = random.randint(0,len(list_of_names)-1)
    return list_of_names[num]

def lastname():
    list_of_lastnames = ["Swett","Hazenberg","Soto-ramirez","Kounias","Galluccio","Casarez","Gwynne","Shorack","Judge","Zani","Garballey","Grove","Pinch","Wallace","Faciana","Bysshe","Paarlberg","Hastings","Moeller",
                        "Spaventa","Gottsdanker","Sade","Surey","Viveros-aguilera"]
    num = random.randint(0,len(list_of_lastnames)-1)
    return list_of_lastnames[num]
    
def address():
    addresses = ["Wall-Street","Long Way", "Seahaven", "Litenway"]
    num = random.randint(1,len(addresses)-1)
    anothernum = random.randint(0,300)
    my_add = addresses[num] + " "+ str(anothernum)
    return my_add

def phone():
    my_phone = ""
    
    first = ["555","554","546"]
    middle = ["632","578","799"]
    number = random.randint(0,len(first)-1)
    my_phone += first[number]+"-"
    my_phone += middle[number]+"-"
    for i in range(5):
        num = random.randint(0,9) 
        my_phone +=str(num)
    return my_phone

def drivers_license():
    license_num = random.randint(1000000000,9999999999)
    return license_num

def country():
    countries = ["Isl","USA","DK","DL","FR","JP"]
    num = random.randint(0,len(countries)-1)
    return countries[num]

def zip():
    zip = random.randint(100,999)
    return zip

def birthday():
    num_1 = random.randint(0,2)
    if num_1 == 0:
        num_2 = 0
        date = random.randint(0,29)
    elif num_1 == 1:
        num_2 = random.randint(0,2)
        date = random.randint(0,30)
    elif num_1 == 2:
        num_2 = random.randint(0,7)
        date = random.randint(0,31)

    months = [["Febuary"],["April","September","November"],["January","March","May","June","July","August","Oktober","December"]]
    chosen_month = months[num_1][num_2]
    b_day = str(date) + ". " + chosen_month
    return b_day


def make_client():
    address_list = []
    phone_list = []
    driver_lc_list = []
    name_list = []
    with open("clients.txt", "w") as my_text:
        for _ in range(100):
            chosen_address = address()
            chosen_phone = phone()
            drivers_ln = drivers_license()
            first_name = firstname()
            last_name = lastname()
            full_name = first_name + " " + last_name
            chosen_country = country()
            chosen_zip = zip()
            chosen_birthday = birthday()
            if chosen_address not in address_list and chosen_phone not in phone_list and  full_name not in name_list and  drivers_ln not in driver_lc_list:
                final = "{},{},{},{},{},{},{}".format(full_name, chosen_address, chosen_phone , chosen_birthday , drivers_ln , chosen_country, chosen_zip)
                #print(final)
                my_text.write(final)
                my_text.write("\n")
            name_list.append(full_name)
            driver_lc_list.append(drivers_ln)
            address_list.append(chosen_address)
            phone_list.append(chosen_phone)
        
make_client()