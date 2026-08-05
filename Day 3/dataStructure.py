'''
n=int(input("Enter the len of arr :"))
arr=[]
for i in range(n):
    num=int(input("Enter the elements in an arr :"))
    arr.append(num)
print(arr)
'''
"""Dulplicate
dulplicate =[]
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            dulplicate.append(arr[i])
            break
print("duplicate element :",dulplicate) """
""" second largest
arr.sort()
print("Array of second largest element in arrary :",arr[n-2])

largest = arr[0]
sec_largest = arr[1]
if largest < sec_largest:
    largest, sec_largest = sec_largest, largest
for num in arr:
    if num > largest:
        sec_largest=largest
        largest=num
    elif num>sec_largest and num!=largest:
        sec_largest=num

print("Second largest element in array :",sec_largest)
"""

"""count of even and odd number in an array"""
"""even_count=0
odd_count=0
for num in arr:
    if num%2==0:
        even_count+=1
    elif num%2!=0:
        odd_count+=1
    
print(f"even count is :{even_count}")
print(f"odd count is :{odd_count}")"""

"""reverse an  array
start=0
end=len(arr)-1
while start < end:
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end-=1
    
print("array reverse :",arr)"""

#print("reverse array :",arr[::-1])slicing method

#linear search
"""
key=int(input("Enter the key to search :"))
found=False
for num in range(len(arr)):
    if arr[num]==key:
        print("key is found")
        found=True
        break

if not found:
    print("key is not found")
"""
#Binary seearch
a=[10,20,30,40,50]
low=0
high=len(a)-1

found =False
print(a)
key=int(input("Enter key element to search :"))
while low <= high:
    mid=(low+high)//2
    if key==a[mid]:
        print(f"key is found {key}")
        found=True
        break
    elif key > a[mid]:
        low = mid+1
    elif key <a[mid]:
        high=mid-1
    
if not found:
    print("key is not found")