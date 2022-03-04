def sumset_sum_count(arr , s , n):
    dp=[[0]*(s+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if i==0:
                dp[i][j]=0
            if j ==0:
                dp[i][j] = 1
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][s]

arr = [9, 7, 0, 3, 9, 8, 6, 5, 7, 6]
s = 31
n =len(arr)
print(sumset_sum_count(arr , s , n))
