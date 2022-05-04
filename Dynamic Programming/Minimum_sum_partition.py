import math

def subset_sum(arr , sum_ , n):
    dp = [[0]*(sum_+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(sum_+1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1
    for i in range(1,n+1):
        for j in range(1,sum_+1):
            if arr[i-1] <= sum_:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    row = []
    m = sum_//2
    for j in range(m+1):
        if dp[i][j]==1:
            row.append(j)
    return row

def minDifference(arr , n):
    row = subset_sum(arr,sum(arr),len(arr))
    min_val = math.inf
	    
    for i in row:
        x = sum(arr)-(2*i)
        if x<  min_val :
            min_val= x
    return min_val

arr = [5, 6, 6, 5, 7, 4, 7, 6]
print(minDifference(arr, len(arr)))
