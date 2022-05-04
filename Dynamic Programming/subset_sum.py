def SubsetSum(arr, sum_):
        n = len(arr)
        count_ =0
        dp = [[0]*(sum_+1) for _ in range (n+1)]
        
        for i in range(n+1):
            for j in range(sum_+1):
                if i == 0:
                    dp[i][j] =0
                if j ==0:
                    dp[i][j] = 1
                
        for i in range(1,n+1):
            for j in range(1,sum_+1):
                if arr[i-1] <= sum_:
                    dp[i][j] = (dp[i-1][j-arr[i-1]] or dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        
        for row in dp:
                print(row)
        
        return dp[i][j]
        


if __name__ == "__main__":
    n , sum_ = 6, 9 #list(map(int ,input().split()))
    arr = [3,34,4,12,5,2] #list(map(int ,input().split()))
    print(SubsetSum(arr, sum_))
    
