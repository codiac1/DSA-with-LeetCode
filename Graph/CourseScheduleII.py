from collections import deque
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegree = {}
        sorted_arr = []
        
        q = deque()
        
        for i in range(n):
            indegree[i] = 0
            graph[i] = list()
        
        for course in prerequisites:
            parent = course[1]
            child = course[0]
            indegree[child] += 1
            graph[parent].append(child)
        
        for v in indegree:
            if indegree[v] == 0:
                q.append(v)
            
        while(q):
            ele = q.popleft()
            sorted_arr.append(ele)
            children = graph[ele]
            for child in children:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        
        if len(sorted_arr) == n:
            return sorted_arr
        return []
