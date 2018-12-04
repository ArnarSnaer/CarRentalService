def readFile(filename): # Create a dictionary with all people and countries out of the file
    the_file = open(filename, "r")
    person_list = dict()
    country_list = []
    for line in the_file:
        split_line = line.split() # Every line is split into two values in a list
        if split_line[0] not in person_list: # New name and value created in the dictionary if name not in dict
            this_person_set = []  # A key's value
            person_list[split_line[0]] = this_person_set 
        if split_line[1] not in person_list[split_line[0]]: # New country to a name if not in name's values
            person_list[split_line[0]].append(split_line[1])
    return person_list

def findHigh(a_dict): # Finding the person with the most countries visited
    high = ""
    highest = 0
    for key,value in a_dict.items():
        if len(value) > highest:
            high = key
            highest = len(value)
    return high, highest

def printResults(a_dict, the_person, the_count, order): # Print out the list
    for name in order:
        print("{}: ".format(name))
        sorted_countries = sorted(a_dict[name]) # Finds the name in the dictionary and sorts their countries in alphabetical order.
        for country in sorted_countries:
            print("\t{}".format(country))

    print("")
    print("{} has been to {} countries".format(the_person, the_count))
        

def main():
    fileName = "flights.txt"
    the_dict = readFile(fileName)
    sorted_names = sorted(the_dict) # Sort the names of the keys in the dictionary in alphabetical order
    high_person, count = findHigh(the_dict)
    printResults(the_dict, high_person, count, sorted_names)

main()