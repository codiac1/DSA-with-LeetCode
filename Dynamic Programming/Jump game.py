class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        n = len(nums)-1
        for i in range(n):
            if i <= reachable:
                reachable = max(reachable , i+nums[i])
            else:
                return False
        if reachable >= n:
            return True
        return False
                    
