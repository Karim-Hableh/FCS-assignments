list=[-12,4,12,25,67]
repeat=True

while repeat==True:
    number=int(input("Enter a number:"))

    if(number==-99):
        repeat=False

    else:
        list.append(number)
        list.sort()
        print(list)