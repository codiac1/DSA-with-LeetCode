class Solution:
    def solve(self , word1, word2, n, m):
        if m == 0 :
            return n
        if n == 0 :
            return m
        if self.dp[n][m] != -1:
            return self.dp[n][m]
        if word1[n-1] == word2[m-1]:
            self.dp[n][m] = self.solve(word1, word2, n-1, m-1)
        else:
            self.dp[n][m] = (1+ min(self.solve(word1, word2, n-1, m) , self.solve(word1, word2, n, m-1)))
        
        return self.dp[n][m]
    
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n == 0 and m == 0:
            return 0 
        if n == 0 :
            return m
        if m == 0 :
            return n
        self.dp = [[-1]*(m+1) for i in range(n+1)]
        return self.solve(word1, word2, n, m)
