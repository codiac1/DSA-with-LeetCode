"""
def binarySearch(row):
    low = 0
    high = len(row)-1
    while (low < high):
        mid=(low+high)//2
        if row[mid] < 0:
            high = mid
        elif row[mid] >= 0:
            low = mid + 1
    return high if row[high] <0 else 0

row1 = [3,2]
row2 = [1,0]


def binarySearch(row,low,high):
    if(low <= high):
        mid=(low+high)//2
        if mid ==0 or row[mid] == 1 and row[mid+1]== 0:
            return mid
        if row[mid] == 0:
            return binarySearch(row,low,mid-1)
        else:
            return binarySearch(row,mid+1,high)
    return "No 1"
row1 = [1,1,1,0,0,0,0,0]
row2 = [1,1,1,1,1,1,0,0,0,0,0]
print(binarySearch(row1,0,len(row1)))
print(row2)
print(binarySearch(row2,0,len(row2)))
"""


def BinarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while (low < high):
        mid = (low + high)//2
        print(mid)
        if (x == arr[mid]):
            return mid
        elif (x > arr[mid]):
            low = mid
        else:
            high = mid - 1
    
    return -1

row1 = [2,3,4]
row2 = [2,7,11,15]
print(row1)
print(BinarySearch(row1,4))
print(row2)
print(BinarySearch(row2,7))

