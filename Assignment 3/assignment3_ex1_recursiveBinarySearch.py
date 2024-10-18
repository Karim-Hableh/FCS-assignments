def recursionBinarySearch(list,key,start,end):
    if start>end:
        return False
    
    mid=(start+end)//2

    if list[mid]==key:
        return True
    elif list[mid]<key:
        return recursionBinarySearch(list,key,mid+1,end)
    else:
        return recursionBinarySearch(list,key,start,mid-1)
    

list=[2,4,33,55,75,80,90,99]
print(recursionBinarySearch(list,75,0,len(list)-1))
print(recursionBinarySearch(list,4,0,len(list)-1))
print(recursionBinarySearch(list,-1,0,len(list)-1))
print(recursionBinarySearch(list,1001,0,len(list)-1))
print(recursionBinarySearch(list,99,0,len(list)-1))