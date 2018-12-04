def Find_client(name):
    client_file = open("clients.txt", "r")
    client_text = str(client_file)
    client_list = client_text.split("\n")
    found_client = ""
    for person in client_list:
        man = str(person)
        if man[0] == name:
            found_client = man
    client_file.close()
    return found_client
    
#Tekur inn nafn af viðskiptavin, rennur því nafni í gegnum skránna með öllum
#viðskiptavinum og finnur hann. Tekur allar upplýsingar hans og skilar þeim.  