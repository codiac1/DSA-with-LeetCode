from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        inDegree = {}
        sorted_arr = []
        
        q = deque()
        
        for i in range(numCourses):
            inDegree[i] = 0
            graph[i] = list()
            
        for course in prerequisites:
            parent = course[0]
            child = course[1]
            inDegree[child] += 1
            graph[parent].append(child)
            
        for v in inDegree:
            if inDegree[v] == 0:
                q.append(v)
        
        while(q):
            ele = q.popleft()
            sorted_arr.append(ele)
            children = graph[ele]
            for child in children:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    q.append(child)
        
        if len(sorted_arr) == numCourses:
            return True
        return False
                    
                
                
