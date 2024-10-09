list1 = [54,76,2,4,98,100]
int1=int(input("Select the first integer:"))
int2=int(input("Select the second integer:"))

for i in list1:
    if(int1<i<int2):
        print(i)