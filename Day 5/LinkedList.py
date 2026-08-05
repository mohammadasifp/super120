class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
        
node1 = Node(15)
node2 = Node(25)
node3 = Node(35)
node4 = Node(45)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=None

class LinkedList:
    def __init__(self):
        self.head = None
    #displaying the linked list
    def displayLL(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    #inserting a new node at the first of the linked list    
    def CreateNewNodeAtFirst(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def InsertNewNodeAtLast(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def InsertNewNodeAtPosition(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head=new_node
            return
        else:
            current = self.head
            while position > 1 and current is not None:
                current = current.next
                position -= 1
            new_node.next = current.next
            current.next = new_node
            
    def DeleteNodeAtBeginning(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        self.head = self.head.next
    
    def DeleteNodeAtEnd(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        else:
            current = self.head
            while current.next is not None:
                prev = current
                current = current.next
            prev.next = None
        print(f"Node deleted at the end of the linked list with value: {current.data}")
    def DeleteNodeAtPosition(self, position):
        if self.head is None:
            print("Linked List is Empty")
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        while position > 1 and current is not None:
            current = current.next
            position -= 1
        if current is None or current.next is None:
            print("Position out of range")
            return
        print(f"Node deleted at position {position} of the linked list with value: {current.next.data}")
        current.next = current.next.next
         
        #current = None
        
        

# Create a LinkedList instance
ll = LinkedList()
ll.head = node1

ll.displayLL()
created_node = ll.CreateNewNodeAtFirst(5)
ll.displayLL()
last_node = ll.InsertNewNodeAtLast(55)
ll.displayLL()
position_node = ll.InsertNewNodeAtPosition(25, 2)
ll.displayLL()
ll.DeleteNodeAtBeginning()
ll.displayLL()  
ll.DeleteNodeAtEnd()
ll.displayLL()  
ll.DeleteNodeAtPosition(1)
ll.displayLL()