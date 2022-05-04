import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -(math.inf)
        curr_sum = 0
        for i in nums:
            curr_sum += i
            max_sum = max(max_sum , curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
