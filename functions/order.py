import datetime

def orders(bilnr, input_start, input_end):

    with open("order.txt", 'r') as test_file:
        is_free = True
        for line in test_file:            
            pn, bn, start, end, name = line.split(',')
''' datetime.datetime.strptime() breytir "1999 03 07" í datetime instance af 1999-03-07 00:00:00'''
            order_start = datetime.datetime.strptime(start, '%Y %m %d')
            order_end = datetime.datetime.strptime(end, '%Y %m %d')
            input_start = datetime.datetime.strptime(input_start, '%Y %m %d')
            input_end = datetime.datetime.strptime(input_end, '%Y %m %d')

            if bilnr == bn:
                while input_start != input_end:
                    current_date = order_start 
                    while current_date != order_end:
                        if current_date == input_start:
                            is_free = False
                        current_date += datetime.timedelta(days = 1)
                    input_start += datetime.timedelta(days = 1)
        # bæta við order í order.txt ef is_free == False
        print(is_free)
        
bilnr = input("bílnúmer: ")
start_date = input("When is car picked up? Answer in format 'year month day' ")
end_date = input("When is car given back? Answer in format 'year month day' ") 

orders(bilnr, start_date, end_date)