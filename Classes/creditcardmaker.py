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
    num = random.randint(0,len(addresses)-1)
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

def kreditcard():
    card =""

    for i in range(4):
        
        for j in range(4):
            card+= str(random.randint(0,9))
        card += "-"
    return card[:-1]

def timevar():
    time =""

    time+= str(random.randint(1,12))
    time += "/"
    time+= str(random.randint(19,26))
    return time

def securenum():
    return random.randint(100,999)

def make_creditcard():
    cardnum_list = []
    securnum_list = []
    address_list = []
    phone_list = []
    with open("kreditcard.txt", "w") as my_text:
        for i in range(300):
            adress = address()
            phonenum = phone()
            kreditc = kreditcard()
            secure = securenum()
            if adress not in address_list and phone not in phone_list and  kreditcard not in cardnum_list and  securenum not in securnum_list:
                final = "{} {},{},{},{},{},{}".format(firstname(), lastname(), adress, kreditc, phonenum, timevar(), secure)
                # print(final)
                my_text.write(final)
                my_text.write("\n")
            cardnum_list.append(kreditc)
            securnum_list.append(secure)
            address_list.append(adress)
            phone_list.append(phonenum)
        
make_creditcard()