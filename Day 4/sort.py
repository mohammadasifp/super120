def selection(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    
def bubble(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i=j=k=0
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
            
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
            
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1

def partition(arr,low,high):
    pivot=arr[low]
    while low <high:
        while arr[low]<=pivot and low<high:
            low+=1
        while arr[high]>pivot:
            high-=1
        if low<high:
            arr[low],arr[high]=arr[high],arr[low]
    #arr[low],arr[high]=arr[high],pivot
    return high
    
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

arr=[5,4,3,2,1]
selection(arr)
print("After selection sort:", arr)
bubble(arr)
print("After bubble sort:", arr)
insertion(arr)
print("After insertion sort:", arr)
merge_sort(arr)
print("After merge sort:", arr)
arr = quick_sort(arr, 0, len(arr) - 1)
print("After quick sort:", arr)