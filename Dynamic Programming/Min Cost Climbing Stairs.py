class Solution:
    """
    def solve(self, cost , n):
        if n == 0 or n == 1:
            return 0
        return min(cost[n-1]+self.solve(cost, n-1) , cost[n-2]+self.solve(cost , n-2))
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        #;return self.solve(cost , n)
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2 , n+1):
            dp[i] = min(cost[i-1]+dp[i-1] , cost[i-2]+dp[i-2])
        return dp[n]
            
