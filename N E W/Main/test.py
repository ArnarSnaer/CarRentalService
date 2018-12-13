def add_insurance_to_price():
        insurance_price = 0
        applied_insurances = []
        chosen_ins = ""
        choice = ""
        while True:
                print("Current price: {}".format(insurance_price))
                print("Current chosen insurances: {}".format(applied_insurances))
                print("Add insurances to car, or type 'q' to continue\n1. Water Damage insurance: 10'000 ISK\n2. CASCO insurance: 20'000 ISK\n3. Some other insurance: 5'000 ISK")
                choice = input("> Enter choice here: ")
                if choice == ("1" or "Water Damage Insurance"):
                        if "1" in applied_insurances:
                                print("Already registered")
                        else:
                                insurance_price += 10000
                                applied_insurances.append("1")
                                chosen_ins += "Water Damage Insurance,"
                if choice == ("2" or "CASCO insurance"):
                        if "2" in applied_insurances:
                                print("Already registered")
                        else:
                                insurance_price += 20000
                                applied_insurances.append("2")
                                chosen_ins += "CASCO insurance,"
                if choice == ("3" or "Some other insurance"):
                        if "3" in applied_insurances:
                                print("Already registered")
                        else:
                                insurance_price += 5000
                                applied_insurances.append("3")
                                chosen_ins += "Some other insurance,"
                if choice == ("q" or "Q"):
                        break
                else:
                        print("Invalid input/insurance already chosen")

        return insurance_price, chosen_ins[:-1]

test1, test2 = add_insurance_to_price()
print(test1, test2)