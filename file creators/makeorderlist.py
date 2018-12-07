



def main():
    with open("vehicle.txt", "r") as data_stream:
        for line in data_stream:
            line_list = line.split(",") 
            with open("orderlist.txt", "a") as new_stream:
                car_plate = line_list[2]
                new_stream.write(car_plate)
                new_stream.write(": [[],[]]")
                new_stream.write("\n")
           
main()