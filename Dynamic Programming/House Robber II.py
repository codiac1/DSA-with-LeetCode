class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) 
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        possibility1 = self.helper(nums[1:])
        possibility2 = self.helper(nums[:n-1])
        return max(possibility1 , possibility2)
    
    def helper(self , nums):
        n =  len(nums)
        dp = [-1]*(n)
        
        dp[0] = nums[0]
        dp[1] = max(nums[1] , nums[0])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2] , dp[i-1])
        return max(dp[-1], dp[-2])
    """
    #recursive way of doing so
    
        def solve(index , nums):
            n = len(nums)
        
            if index == 0 :
                return nums[0]
            if index < 0 :
                return 0
            if dp[index] != -1:
                return dp[index]
            dp[index] = max(nums[index]+solve(index-2, nums) , solve(index-1 , nums))
            return dp[index]
        
        return solve(n-1 , nums)
        """
        
