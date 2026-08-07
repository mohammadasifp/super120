""". Write a Python program to merge two queues into a single queue while preserving the order of elements.
Example
Queue 1: 10 20 30
Queue 2: 40 50 60
Output:
10 20 30 40 50 60
"""

queue1=[10,20,30,40,50]
queue2=[40,50,60]
queue3=[]

for i in range(len(queue1)):
    queue3.append(queue1[i])
    
for j in range(len(queue2)):
    queue3.append(queue2[j])
    
print(queue3)