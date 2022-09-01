class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        
        def solve(n , m):
            if n <= 0 :
                return m
            if m <= 0 :
                return n
            
            if dp[n][m] != -1:
                return dp[n][m]
            
            if word1[n-1] == word2[m-1]:
                dp[n][m] =  solve(n-1 , m-1)
            
            else:
                dp[n][m] = 1 + min(solve(n-1 , m-1) , min(solve(n-1 , m) , solve(n , m-1)))
            return dp[n][m]
        
        
        return solve(n , m)
