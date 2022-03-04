def findElement(arr, n):
    min_array = []
    max_array = []
    max_now = arr[0]
    min_now = arr[-1]
    for i in range(n):
        if arr[i] > max_now:
            max_now = arr[i]
        max_array.append(max_now)
    for i in range(n-1 , -1 ,-1):
        if arr[i] < min_now:
            min_now = arr[i]
        min_array.append(min_now)
    print("max_array :" , max_array)
    print("min_array :" , min_array)
    for i in range(n):
        if min_array[n-i-1] == max_array[i] and i!=0 and i!=n-1:
            return max_array[i]
    return -1

arr = [6 , 1 , 10]
c = findElement(arr , 3)
print(c)
