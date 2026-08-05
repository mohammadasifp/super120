'''def search(Roll_Numbers, Search_Roll_Number):
    low = 0
    high =len(Roll_Numbers) - 1
    while low <= high:
        mid=(low+high)//2
        if Roll_Numbers[mid]==Search_Roll_Number:
            return mid
        elif Roll_Numbers[mid]>Search_Roll_Number:
            high=mid-1
        else:
            low = mid+1
    return -1


Roll_Numbers = [101, 105, 110, 115, 120]
Search_Roll_Number=110
search_result = search(Roll_Numbers, Search_Roll_Number)
if search_result != -1:
    print(f"Roll number {Search_Roll_Number} found at index {search_result}.")
else:
    print(f"Roll number {Search_Roll_Number} not found in the list.")'''
    
def FindMin(Temp):
    min=Temp[0]
    for i in range(len(Temp)):
        if Temp[i]<min:
            min=Temp[i]
    print("Minimum Temperature is:",min)
Temperatures=[34, 29, 31, 27, 35, 30]
FindMin(Temperatures)