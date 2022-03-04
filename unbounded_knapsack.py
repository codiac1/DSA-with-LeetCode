def unbounded_knapsack(wt , val , W , n):
    dp = [[0]*(W+1) for i in range(n+1)]
     
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<= j:
                dp[i][j] = max(val[i-1] +dp[i][j-wt[i-1]] , dp[i-1][j] )
            else:
                dp[i][j] =  dp[i-1][j]
    return dp[n][W]

wt = [1,3,4,5,9]
val = [10,40,50,70,60]
W = 8
n=len(wt)
print(unbounded_knapsack(wt , val , W , n))
