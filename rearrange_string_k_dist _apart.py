from heapq import *
from collections import deque
def reorganizeString(s,k):
    fmap = {}
    max_heap = []
    prevchar = None
    prevfreq = 0
    result = []
    for i in s:
        fmap[i] = fmap.get(i, 0) + 1

    for char, freq in fmap.items():
        heappush(max_heap, (-freq, char))

    q = deque()

    while(max_heap):
        currfreq , currchar = heappop(max_heap)
        result.append(currchar)
        q.append((currchar, currfreq+1))
        if len(q) == k:
            ch , f = q.popleft()
            if -f > 0:
                heappush(max_heap , (f , ch))
    return ''.join(result) if len(result) == len(s) else ""

s = "abccd"
print(reorganizeString(s,3))
