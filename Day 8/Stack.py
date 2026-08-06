class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        if not self.isFull():
            self.stack.append(item)
            print(f"{item} is push an stack scuessfullt")
        else:
            print("stack is full can not push element")
    def pop(self):
        if not self.isEmpty():
            print("poped element is ",self.stack.pop())
        else:
            print("stack is empty ")
    def peek(self):
        if not self.isEmpty():
            print(f"the stack top elements is :{self.stack[-1]}")
        else:
            print("stack is empty ")
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def isFull(self):
        if len(self.stack)==5:
            return True
        else:
            return False
        
    def display(self):
        if not self.isEmpty():
            print("the stack elements are :",self.stack)
        else:
            print("stack is empty ")

s=Stack()
n=int(input("Enter the number of elements you want to push in stack :"))
for i in range(n):
    item=int(input("Enter the value :"))
    s.push(item)
s.display()
s.pop()
s.peek()
s.display()