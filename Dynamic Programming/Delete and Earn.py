class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq= {}
        for i in nums:
            freq[i] = freq.get(i , 0)+1
        #print(freq)
        nums = sorted(set(nums))

        n = len(nums)
        
        dp = [0]*(n+1)
        dp[1] = nums[0]*freq[nums[0]]
        
        for i in range(1,n): 
            points = freq[nums[i]]*nums[i]
            if nums[i]-1 == nums[i-1]:
                dp[i+1] = max(dp[i] , dp[i-1]+points)
            else:
                dp[i+1] = dp[i]+points
        return dp[-1]
                
