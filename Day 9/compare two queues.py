"""Write a Python program to compare two queues and determine whether they contain the same elements in the same order.
Example
Queue 1: 10 20 30
Queue 2: 10 20 30
Output:
Queues are Equal
"""

queue1=[10,20,30]
queue2=[10,20,30]

queue1 = [10, 20, 30]
queue2 = [10, 20, 30]

if len(queue1) != len(queue2):
    print("Queues are not Equal")
else:
    equal = True

    for i in range(len(queue1)):
        if queue1[i] != queue2[i]:
            equal = False
            break

    if equal:
        print("Queues are Equal")
    else:
        print("Queues are not Equal")