def canPartition(nums):
    if sum(nums)%2 != 0 :
        return False
    else:
        s = sum(nums)//2
        n = len(nums)
        dp = [[0]*(s+1) for i in range(n+1)]
        for i in range(n+1):
            for j in range(s+1):
                if i ==0:
                    dp[i][j] = False
                if j==0:
                    dp[i][j] = True
        for i in range(1,n+1):
            for j in range(1,s+1):
                if nums[i-1] <= s:
                    dp[i][j] = (dp[i-1][j-nums[i-1]] or dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[i][j]

if __name__ == "__main__":
    arr = [2,6,3,9,4,1,5]
    print(canPartition(nums))