class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        e1 = edges[0]
        e2 = edges[1]
        
        if e1[0]==e2[0]:
            return e1[0]
        elif e1[0]==e2[1]:
            return e1[0]
        else:
            return e1[1]
        
