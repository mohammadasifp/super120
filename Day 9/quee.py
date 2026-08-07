class Queue:
    def __init__(self):
        self.queue=[]
        
    def enqueue(self,item):
        if not self.isFull():
            self.queue.append(item)
            print(f"{item} is enqueue an queue scuessfully")
        else:
            print("queue is full can not enqueue element")
            
    def dequeue(self):
        if not self.isEmpty():
            print(self.queue.pop(0),"dequeue the element in a queue")
        else:
            print("queue is Empty")
            
    def display(self):
        if not self.isEmpty():
            print("queue elements are :\n",self.queue)
        else:
            print("queue is Empty")
            
    def peek(self):
        if not self.isEmpty():
            print("queue elements are :\n",self.queue[0])
        else:
            print("queue is Empty")
    
    def isEmpty(self):
            if len(self.queue)==0:
                return True
            else:
                return False
    def isFull(self):
        if len(self.queue)==5:
            return True
        else:
            return False
        
    def reverse(self):
        print("Reverse all the element in a queue :")
        for i in range(len(self.queue)-1,-1,-1):
            print(self.queue[i],end = " -> ")
        print("None")
        
    def EvenOdd(self):
        even=[]
        odd=[]
        for i in range(len(self.queue)-1):
            if self.queue[i]%2==0:
                even.append(self.queue[i])
            else:
                odd.append(self.queue[i])
        print("Even elements in a queue are :",even)
        print("Odd elements in a queue are :",odd)
qq=Queue()
n=int(input("Enter the number of n:"))
for i in range(n):
    item = int(input("Enter the value :"))
    qq.enqueue(item)
    
    
qq.display()
qq.dequeue()
qq.display()
qq.peek()
qq.reverse()
qq.EvenOdd()