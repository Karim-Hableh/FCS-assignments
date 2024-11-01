dic1={
    "karim":22,
    "yehya":25,
    "abed":18,
    "bassem":75,
    "hala":60
}
print(dic1.values())

def search(dictionary):
    max_age=int()
    max_name=str()

    for name,age in dictionary.items():
       if age>max_age:
           max_age=age
           max_name=name
    return max_name

result=search(dic1)
print(result)