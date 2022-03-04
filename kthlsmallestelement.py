from heapq import *
def findKthSmallest(nums, k) :
    max_heap = []
    for i in range(k):
        heappush(max_heap, -nums[i])
    for j in range(k,len(nums)):
        if -nums[j]>max_heap[0]:
            heappop(max_heap)
            heappush(max_heap , -nums[j])
    return -max_heap[0]

arr = [8,9,3,0,1,67,23]
print(findKthSmallest(arr , 3))
