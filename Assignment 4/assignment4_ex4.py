class Node:
    def __init__(self,info,next):
        self.info=info
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0 # count the number of nodes in the LL

    def append(self,val): #O(1)
        if self.size==0: # no nodes in the LL
            n=Node(val,None)
            self.head=n
            self.tail=n
            self.size+=1
        else:
            n=Node(val,None)
            self.tail.next=n
            self.tail=n
            
        self.size+=1

    def deleteAtLocation(self,location):
        if self.size==0:
            print("The list is empty.")
            return
        
        if location == 0:
            self.head = self.head.next
            return
        
        current=self.head
        for i in range(location-1):
            if current==0 or current.next==0:
                 print("Location is out of bounds.")
                 return
            current = current.next


        if current.next is None:
            print("Location is out of bounds.")
            return
        
        current.next = current.next.next

    def printLL(self):
        tmp=self.head
        while(tmp!=None):
            print(tmp.info,"->")
            tmp=tmp.next

ll = LinkedList()

ll.append(12)
ll.append(56)
ll.append(76)
ll.append(11)
ll.append(0)

print("Original Linked List:")
ll.printLL()

ll.deleteAtLocation(0)
print("\nLinked List after deleting node at location 0:")
ll.printLL()

ll.deleteAtLocation(3)
print("\nLinked List after deleting node at location 3:")
ll.printLL()

        
