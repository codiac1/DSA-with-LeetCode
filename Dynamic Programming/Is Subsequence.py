class Solution:
    def lcs(self , s , t):
        n, m = len(s),len(t)
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range( 1,m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        index = dp[n][m]-1
        result = ["_"]*(index+1)
        i = n
        j = m
        while(i>0 and j>0):
            if s[i-1] == t[j-1] :
                result[index] = s[i-1]
                index -= 1
                i -= 1
                j -= 1 
            elif dp[i-1][j]>dp[i][j-1]:
                i = i-1
            else:
                j = j-1
        result = "".join(result)
        if s == result:
            return True
        return False
    
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 :
            return True
        if len(s) != 0 and len(t) == 0:
            return False
        return self.lcs(s , t)
