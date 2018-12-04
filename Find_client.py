def Find_client(name):
    client_text = open(client_list.txt, r)
    client_list = client_text.split("\n")
    for person in client_list:
        if person[0] == name:
            found_client = person
    return person
    
#Tekur inn nafn af viðskiptavin, rennur því nafni í gegnum skránna með öllum
viðskiptavinum og finnur hann. Tekur allar upplýsingar hans og skilar þeim.    
