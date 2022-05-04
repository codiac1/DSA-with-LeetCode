class Solution:
    """
    def climb(self,n):
        if n == 1 or n ==2:
            return n
        if self.dp[n] != -1:
            return self.dp[n]
        
        self.dp[n] = self.climb(n-1) + self.climb(n-2)
        return self.dp[n]
    """
    
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        self.dp = [-1]*(n+1)
        #return self.climb(n)
        for i in range(3):
            self.dp[i] = i
        
        for i in range(3,n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[n]
