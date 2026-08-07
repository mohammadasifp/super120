"""Write a Python program to compare two queues and determine whether they contain the same elements in the same order.
Example
Queue 1: 10 20 30
Queue 2: 10 20 30
Output:
Queues are Equal
"""

queue1=[10,20,30]
queue2=[10,20,30]

for i in range(len(queue1)):
    for j in range(len(queue2)):
        if queue1[i]==queue2[j]:
            print("Queues are Equal")
else:
    print("Queues are not Equal")
            