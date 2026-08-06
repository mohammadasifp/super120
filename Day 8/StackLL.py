class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class StackLL:
    def __init__(self):
        self.head=None
        
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        
    def pop(self):
        if self.head is None:
            print("Stack is Empty")
            return

        value = self.head.data
        self.head = self.head.next
        return value
    
    def peek(self):
        if self.head is None:
            print("Stack is Empty")
            return
        print("Satck top element is ",self.head.data)
    
    def display(self):
        if self.head is None:
            print("Stack is empty")
            return
        print("Stack elemts are :")
        temp=self.head
        while temp != None:
            print(temp.data ,end=" -> ")
            temp=temp.next
        print()
        
    def reverse(self):
        if self.head is None:
            print("Stack is empty")
            return
        temp=self.head
        while temp != None:
            temp=temp.next
        for i in range(temp,-1,-1):
            print(self.stack(i))
            
s=StackLL()
n=int(input("Enter the number of elements you want to push in stack :"))
for i in range(n):
    item=int(input("Enter the value :"))
    s.push(item)
s.display()
s.pop()
s.peek()
s.display()    