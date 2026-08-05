class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DDL:
    def __init__(self):
        self.tail=None
        self.head=None
    
    def createNewNodeAtFirst(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            
    def createNewNodeAtLast(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
            
    def insertAtEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            temp=self.head
            while temp != None:
                temp=temp.next
            newNode.prev=temp
            self.tail.next=newNode
            self.tail=newNode
            
            
    def displayDLL(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
            return
        current=self.head
        while current:
            print(current.data,end=" <-> ")
            current=current.next
        print("None")
        
    def displayDLLReverse(self):
        if self.tail is None:
            print("Doubly Linked List is Empty")
            return
        current=self.tail
        while current:
            print(current.data,end=" <-> ")
            current=current.prev
        print("None")
    def deleteAll(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
            return
        current=self.head
        while current:
            next_node=current.next
            del current
            current=next_node
        self.head=None
        self.tail=None
        print("All nodes deleted successfully")
        
    def countNodes(self):
        count=0
        temp=self.head
        while temp != None:
            count+=1
            temp=temp.next
        return count
    
    def minMax(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
            return
        minVal=self.head.data
        maxVal=self.head.data
        temp=self.head
        while temp != None:
            if temp.data < minVal:
                minVal = temp.data
            if temp.data > maxVal:
                maxVal = temp.data
            temp = temp.next
        print("Minimum value:", minVal)
        print("Maximum value:", maxVal)
        
    def swap(self,x,y):
        if x == y:
            return
        # Find nodes with values x and y
        nodeX = self.head
        nodeY = self.head
        while nodeX and nodeX.data != x:
            nodeX = nodeX.next
        while nodeY and nodeY.data !=y:
            nodeY = nodeY.next
        if nodeX is None or nodeY is None:
            print("One or both values not found in the list.")
            return
        # Swap the nodes
        if nodeX.prev:
            nodeX.prev.next = nodeY
        else:
            self.head = nodeY

        if nodeY.prev:
            nodeY.prev.next = nodeX
        else:
            self.head = nodeX

        # Swap the next pointers
        temp = nodeX.next
        nodeX.next = nodeY.next
        nodeY.next = temp

        # Swap the prev pointers
        temp = nodeX.prev
        nodeX.prev = nodeY.prev
        nodeY.prev = temp
        
    def sumofall(self):
        if self.head == None:
            print("List is empty")
            return
        else:
            sum=0
            currentNode=self.head
            while currentNode != None:
                sum += currentNode.data
                currentNode=currentNode.next
            print("Sum all node in linked list is :",sum)
    def MoveLasttoFirst(self):
        if self.head == None:
            print("List is empty")
            return
        else:
            current = self.tail
            current.prev.next = None
            current.prev = None
            current.next = self.head
            self.head.prev = current
            self.head = current
            

new_dll=DDL()
n=int(input("Enter the number of nodes you want to create: "))
for i in range(n):
    data=int(input(f"Enter the value for node {i+1}: "))
    new_dll.createNewNodeAtLast(data)   
new_dll.displayDLL()
print("Number of nodes:", new_dll.countNodes())
new_dll.minMax()

new_dll.createNewNodeAtFirst(5)
new_dll.displayDLL()
new_dll.swap(5, 3)
new_dll.displayDLL()
new_dll.sumofall()
new_dll.MoveLasttoFirst()
new_dll.displayDLL()