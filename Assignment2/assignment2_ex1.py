list1 = [54,76,2,4,98,100]
int1=int(input("Select the first integer:"))
int2=int(input("Select the second integer:"))

if int1>int2:
    tmp=int1
    int1=int2
    int2=tmp
print(f"int1 will be {int1} and int2 will {int2}")
for i in list1:
    if(int1<i<int2):
        print(i)