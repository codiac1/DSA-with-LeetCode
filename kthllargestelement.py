from heapq import *
def findKthLargest(nums, k) :
    min_heap = []
    for i in range(k):
        heappush(min_heap,nums[i])
    for j in range(k,len(nums)):
        if nums[j]>min_heap[0]:
            heappop(min_heap)
            heappush(min_heap , nums[j])
    return min_heap[0]

arr = [8,9,3,0,1,67,23]
print(findKthLargest(arr , 3))
