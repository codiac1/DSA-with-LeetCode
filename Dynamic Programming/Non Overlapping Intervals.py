class Solution:
    def eraseOverlapIntervals(self, nums: List[List[int]]) -> int:
        c = 0
        if len(nums)==1 or len(nums)==0 :
            return 0
        nums.sort(key = lambda x: x[0])
        i = 1
        min_= nums[0][1]
        while(i<len(nums)):
            if nums[i][0] < min_ :
                c += 1
                min_ = min(min_ , nums[i][1])
            else:
                min_ = nums[i][1]
            i+=1
        return c
    #[[1, 2], [2, 3], [1, 3], [3, 4]]
