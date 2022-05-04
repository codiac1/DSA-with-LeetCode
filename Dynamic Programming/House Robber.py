class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        def solve(index):
            if index == 0:
                return nums[index]
            if index < 0:
                return 0
            if dp[index] != -1:
                return dp[index]
                
            dp[index] = max(solve(index-2) + nums[index], solve(index-1))
            return dp[index]
             
        return solve(n-1)
    
