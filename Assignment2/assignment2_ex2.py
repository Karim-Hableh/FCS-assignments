Names= ["Maria","Hala","Ghady","Ehsan","Joe","Zoe"]
while(True):
    letter=input("Select a letter:")
    for i in Names:
        if i.__contains__(letter):
            print(i)
