import datetime 


times = datetime.date(1999,2,12)
print(times)
''' print fallið gefur 1999-02-12'''


timestr = "1999 02 12"
timestr = timestr
redo_time = datetime.datetime.strptime(timestr, '%Y %m %d')
print(redo_time)
