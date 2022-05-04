class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        t = ""
        for i in s:
            t = i + t
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range( 1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        return dp[n][n]
