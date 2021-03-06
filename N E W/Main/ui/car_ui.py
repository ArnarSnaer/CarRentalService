from services.car_services import Car_services
import os
class Car_UI(object):
    def __init__(self):
        self.car_serv = Car_services()
        self.car_repo = self.car_serv.car_repo
        self.keywords = []
    
    def choose_car(self,results):
        ''' This function takes in a nested list of car information and returns a specific car'''
        counter = 1
        for item in results:
            try:
                car_object = self.car_serv.create_car(item)
                veh_type = self.car_repo.car_model.get_veh_type(car_object)
                brand = self.car_repo.car_model.get_brand(car_object)
                plate = self.car_repo.car_model.get_plate(car_object)
                price = self.car_repo.car_model.get_price(car_object)
                price = price[:-1]
                if self.car_repo.car_model.get_status(car_object) == "True":
                    status = "Available."
                else:
                    status = "Unavailable."
                print("{:>5d}. {} Type: {:>5s}{:>5s}Brand: {:>5s}{:>5s}License plate: {:>5s}{:>5s}Base price: {:>5s}{:<5s}Current status: {:>5s}".format(counter,"|",veh_type,"", brand,"", plate,"", price,"", status))
                counter += 1
            except Exception:
                pass

        quit = False
        print("Complete! Here are all the results of the search.\n")
        while not quit:
            choice = input("What car would you like to choose? (enter 'q' to quit): ")
            if choice == 'q':
                quit = True
                print("Car not chosen aborting order") 
                return None
            elif  int(choice) in range(counter+1):    
                choice_int = int(choice)
                return results[choice_int-1]
            else:
                print("Please input a valid integer")
        
    def car_menu(self):
        '''A function that creates a menu for car'''
        choice = ""

        while choice != "q":
            print("\nCurrent section: Cars\n1. Add a new car into the database\n2. Remove a car from the database\n3. Search car database\n4. See all cars in the current database\n5. See all available cars\n6. See all unavailable cars\nq. Back")
            choice = input("> What would you like to do? ").lower()
            
            '''When selected to add a new car to the database'''
            if choice == "1":
                print("New car will be added into the database.\nOnly write the names or numbers of the options. Wrong input will result in going back to the main menu.\n")
                choose_veh_type = input("Available vehicle types:\n1. Sedan\n2. SUV\n3. MPV\n4. Mini\n5. Sport\nAny other input will cancel the other.\n> Choose a type by its name or number: ")
                if (choose_veh_type == "Sedan") or (choose_veh_type == "1"):
                    veh_type = "Sedan"
                elif (choose_veh_type == "SUV") or (choose_veh_type == "2"):
                    veh_type = "SUV"
                elif (choose_veh_type == "MPV") or (choose_veh_type == "3"):
                    veh_type = "MPV"
                elif (choose_veh_type == "Mini") or (choose_veh_type == "4"):
                    veh_type = "Mini"
                elif (choose_veh_type == "Sport") or (choose_veh_type == "5"):
                    veh_type = "Sport"          
                else:
                    print("Wrong input, going back to main menu...\n")
                    break
               
                choose_brand = input("\nAvailable car brands:\n1. Campagna\n2. Suzuki\n3. Ferrari\n4. Audi\n5. Unique\n> Choose a brand by its name or number: ")
                if (choose_brand == "Campagna") or (choose_brand == "1"):
                    brand = "Campagna"
                elif (choose_brand == "Suzuki") or (choose_brand == "2"):
                    brand = "Suzuki"
                elif (choose_brand == "Ferrari") or (choose_brand == "3"):
                    brand = "Ferrari"
                elif (choose_brand == "Audi") or (choose_brand == "4"):
                    brand = "Audi"
                elif (choose_brand == "Unique") or (choose_brand == "5"):
                    brand = "Unique"    
                else:
                    print("Wrong input, going back to main menu...\n")
                    break

                plate = input("\nWhat is the car plate? License plates should have 3 letters followed by 2 numbers\n> Enter car plate here: ")

                print("\nAvailable wheel drives:\n1. 4 Wheel Drive (4WD)\n2. Forward Wheel Drive (FWD)\n3. Rear Wheel Drive (RWD)")
                choose_wheel_drive = input("> Choose a wheel drive by number, full name or abbreviation: ")
                if (choose_wheel_drive == "1") or (choose_wheel_drive == "4 Wheel Drive") or (choose_wheel_drive == "4WD"):
                    wheel_drive = "4WD"
                elif (choose_wheel_drive == "2") or (choose_wheel_drive == "Forward Wheel Drive") or (choose_wheel_drive == "FWD"):
                    wheel_drive = "FWD"
                elif (choose_wheel_drive == "3") or (choose_wheel_drive == "Rear Wheel Drive") or (choose_wheel_drive == "RWD"):
                    wheel_drive = "RWD"
                else:
                    print("Wrong input, going back to main menu...\n")
                    break

                status = "True"

                choose_is_manual = input("\n> Is the car:\n1 Manual (M)\n2. Automatic (A)\n> Answer here: ")
                if (choose_is_manual.upper() == "MANUAL") or (choose_is_manual == "MANUAL") or (choose_is_manual == "Manual") or (choose_is_manual == "1") or (choose_is_manual == "M"):
                    is_manual = "MANUAL"
                elif (choose_is_manual.upper() == "AUTOMATIC") or (choose_is_manual == "AUTOMATIC") or (choose_is_manual == "Automatic") or (choose_is_manual == "2") or (choose_is_manual == "A"):
                    is_manual = "AUTOMATIC"
                else:
                    print("Wrong input, going back to main menu...\n")
                    break

                try:
                    driven = int(input("\nHas the car been driven before?\n> Answer in integers and in KM (Do not answer in negatives): "))
                    if driven < 0:
                        print("Wrong input, going back to main menu...\n")
                        break
                except Exception:
                    print("Wrong input, going back to main menu...\n")
                    break
                
                choose_fuel_type = input("\nAvailable fuel types:\n1. Gazolene (G)\n2. Diesel (D)\n> Answer here: ")
                if (choose_fuel_type == "1") or (choose_fuel_type == "G") or (choose_fuel_type == "Gazolene") or (choose_fuel_type == "gazolene") or (choose_fuel_type.upper() == "GAZOLENE"):
                    fuel_type = "GAZOLENE"
                elif (choose_fuel_type == "2") or (choose_fuel_type == "Diesel") or (choose_fuel_type == "diesel") or (choose_fuel_type.upper() == "DIESEL") or (choose_fuel_type == "D"):
                    fuel_type = "DIESEL"
                else:
                    print("Wrong input, going back to main menu...\n")
                    break

                price = self.car_serv.calculate_price(veh_type)
                print("\nVehicle Type: {}\nCar brand: {}\nLicense plate: {}\nWheel drive: {}\nAuto/Man: {}\nDriven: {}\nFuel type: {}\nCar Price: {}\n".format(veh_type, brand, plate, wheel_drive, is_manual, driven, fuel_type, price))
                confirmation = input("> Is this information correct?(Y/N): ")
                if (confirmation == "Y") or (confirmation == "Yes") or (confirmation == "y"):
                    new_car = self.car_repo.car_model(veh_type, brand, plate, wheel_drive, status, is_manual, driven, fuel_type, price)
                    self.car_repo.add_car(new_car) 
                    print("The car has been successfully updated into the car database")
                elif (confirmation == "N") or (confirmation == "No") or (confirmation == "n"):
                    print("Operation cancelled, going back to Cars section...\n")
                else:
                    print("Invalid input! Write either (Y/N)")
                
                '''When chosen to remove a car'''
            elif choice == "2":
                print("Searching for a specific car.\nYou can search for vehicle type, brand and license plate by their name")
                searchword = input("> Please only enter a single item:  ")
                results = self.car_repo.find_car(searchword)
                if len(results) == 0:
                    print("No results for this search word.\n")
                else:
                    choice = self.choose_car(results)
                    self.car_repo.remove_car(choice[2])
                    print("Car successfully removed.")

                ''' When chosen to Search the car database'''
            elif choice == "3":                
                searchword = input("\n> Insert information as search word; Vehicle type, Brand, License plate, etc\nPlease only enter a single item:  ")
                results = self.car_repo.find_car(searchword)
                if len(results) == 0:
                    print("No results for this search word.\n")
                else:
                    try:
                        car_list = self.choose_car(results)
                        car = self.car_serv.create_car(car_list)
                        veh_type = car.get_veh_type()
                        brand = car.get_brand()
                        plate = car.get_plate()
                        wheel_drive = car.get_wheel_drive()
                        status = car.get_status()
                        if status == "True":
                            status = "Available"
                        else:
                            status = "Unavailable"
                        is_manual = car.get_is_manual()
                        driven = car.get_driven()
                        fuel_type = car.get_fuel_type()
                        price = car.get_price()
                        print("\nCar's information:\n\nVehicle type: {}\nBrand: {}\nCar plate: {}\nWheel Drive: {}\nCurrent status: {}\nManual: {}\nHas been driven(KM): {}\nFuel type: {}\nBase price: {}".format(veh_type,brand,plate,wheel_drive,status,is_manual,driven, fuel_type, price))
                    except Exception:
                        print("No car chosen.")
            
                ''' When chosen from 4-6 '''
            elif (choice == "4") or (choice == "5") or (choice == "6"):
                file_text = self.car_serv.car_repo.get_all_cars()
                number = 1
                for item in file_text:
                    try:
                        car_object = self.car_serv.create_car_from_list(item)
                        veh_type = self.car_repo.car_model.get_veh_type(car_object)
                        brand = self.car_repo.car_model.get_brand(car_object)
                        plate = self.car_repo.car_model.get_plate(car_object)
                        price = self.car_repo.car_model.get_price(car_object)
                        price = price[:-1]
            
            
                        ''' Get all cars in the database '''
                        if choice == "4":
                            if self.car_repo.car_model.get_status(car_object) == "True":
                                status = "Available."
                            else:
                                status = "Unavailable."
                            print("{:>5d}. {} Type: {:>5s}{:>5s}Brand: {:>5s}{:>5s}License plate: {:>5s}{:>5s}Base price: {:>5s}{:<5s}Current status: {:>5s}".format(number,"|",veh_type,"", brand,"", plate,"", price,"", status))
                            number += 1


                            ''' Get all 'Available cars' '''
                        elif choice == "5":
                            if self.car_repo.car_model.get_status(car_object) == "True":
                                status = "Available."
                                print("{:>5d}. {} Type: {:>5s}{:>5s}Brand: {:>5s}{:>5s}License plate: {:>5s}{:>5s}Base price: {:>5s}{:<5s}Current status: {:>5s}".format(number,"|",veh_type,"", brand,"", plate,"", price,"", status))
                                number += 1

                            ''' Get all 'Unavailable cars' '''
                        elif choice == "6":
                            if self.car_repo.car_model.get_status(car_object) == "False":
                                status = "Unavailable."
                                print("{:>5d}. {} Type: {:>5s}{:>5s}Brand: {:>5s}{:>5s}License plate: {:>5s}{:>5s}Base price: {:>5s}{:<5s}Current status: {:>5s}".format(number,"|",veh_type,"", brand,"", plate,"", price,"", status))
                                number += 1
                    except Exception:
                        pass

            elif choice != "q":
                print("Invalid input! Please enter the number/letter in front of each operation!\n")

        print("Going back to main menu...\n")

    def order_menu(self):
        '''Makes an order menu for the Order UI'''
        os.system('cls')
        print("\nAvailable car(s):\n")
        available_cars = self.car_serv.get_available_cars_list()
        chosen_car = self.choose_car(available_cars)
        if chosen_car == None:
            return None
        else:
            rented_car = self.car_serv.create_car(chosen_car)
        return rented_car