def knapsack(wt , val , W , n , dp):
    if n==0 or W == 0:
        dp[n][W] = 0
    if dp[n][W] != -1:
        return dp[n][W]
    if wt[n-1] <= W:
        dp[n][W] = max(val[n-1]+knapsack(wt , val , W-wt[n-1] , n-1 , dp), knapsack(wt , val , W , n-1 , dp))
    else:
        dp[n][W] =  knapsack(wt , val , W , n-1 , dp)
        
    return dp[n][W]

if __name__ == "__main__":
    wt = [2, 3, 1, 4]
    val = [4, 5, 3, 7]
    W = 5
    n = len(wt)
    dp = [[-1]*(W+1) for i in range(n+1)]
    ans = knapsack(wt , val , W , n , dp)
    for row in dp:
        print(row)
    print(ans)

    
