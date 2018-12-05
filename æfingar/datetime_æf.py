from datetime import datetime

date1 = input("Input first date (DD/MM/YYYY): ")
date2 = input("Input second date (DD/MM/YYYY): ")

day1,month1,year1 = date1.split(" ")
day2,month2,year2 = date2.split(" ")

daytime_val1 = datetime(int(year1),int(month1),int(day1))
daytime_val2 = datetime(int(year2),int(month2),int(day2))

daytime_val3 = daytime_val2 - daytime_val1
print(daytime_val1)
print(daytime_val2)
print("")
print(daytime_val3.days)