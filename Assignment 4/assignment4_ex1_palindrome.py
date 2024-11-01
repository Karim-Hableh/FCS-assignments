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
    

def isPalindrome(value):
    if len(value)==0:
        return True
    
    s=Stack()

    for i in value:
        s.push(i)

    for i in value:
        if i!=s.pop():
            return False
    return True

value="moyehyam"
result=isPalindrome(value)
print(result)
        