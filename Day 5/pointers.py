arr=[5, 10, 15, 20, 25 ]
left=0
right=len(arr)-1
target=15

while left<=right:
    sum=arr[left]+arr[right]  
    if sum==target:
        print("Target found ",sum )
        break
    elif sum<target:
        left+=1
    else:
        right-=1
else:
    print("Target not found")