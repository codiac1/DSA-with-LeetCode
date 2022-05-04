import math
class Solution:
    def rmcm(self , arr , i , j, dp):
            if i==j:
                dp[i][j] = 0
            if dp[i][j] != -1:
                return dp[i][j]
            min_ = math.inf
            for k in range(i,j):
                temp = self.rmcm(arr , i , k , dp)+self.rmcm(arr , k+1 , j , dp)+ (arr[i-1]*arr[j]*arr[k])
                if temp< min_:
                    min_ = temp
            dp[i][j] = min_
            return dp[i][j]
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[-1]*n for i in range(n)]
        return self.rmcm(values , 1 , n-1 , dp)
            
            
