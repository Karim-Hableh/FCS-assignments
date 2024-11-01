class Stack:
    def __init__(self):
        self.elements=[]

    def push(self,val):
        self.elements.append(val)

    def pop(self):
        if(len(self.elements)==0):
            return None
        return self.elements.pop()
    
    def isEmpty(self):
        return len(self.elements)==0
    
def decode(value):
    s=Stack()
    for i in value:
        if i ==" " or i.isalpha():
            s.push(i)
        elif i =="*":
            res=s.pop()
            print(res,end="")

    decoded_message = "".join((reversed(s.elements)))
    return decoded_message

input="SIVLE ****** DAED TNSI ***"
result=decode(input)
print(result)