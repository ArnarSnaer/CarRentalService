# import datetime 


# times = datetime.date(1999,2,12)
# print(times)
# ''' print fallið gefur 1999-02-12'''


# timestr = "1999 02 12"
# timestr = timestr
# redo_time = datetime.datetime.strptime(timestr, '%Y %m %d')
# print(redo_time)
open_file = open("bilar.txt", "r")
lines = open_file.readlines()
open_file.close()

open_file = open("bilar.txt", "w")



for line in lines:
    if "KPH38" not in line:
        open_file.write(line)
open_file.close()