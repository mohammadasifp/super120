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
            if len(self.stack)==0:
                return True
            else:
                return False
    def isFull(self):
        if len(self.stack)==5:
            return True
        else:
            return False
        
qq=Queue()
n=int(input("Enter the number of n:"))
for i in range(n):
    item = int(input("Enter the value :"))
    qq.enqueue(item)
    print(f"{item} is add to the queue sucessfully")
    
qq.display()
qq.dequeue()
qq.display()
qq.peek()