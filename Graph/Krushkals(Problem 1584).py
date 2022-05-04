class Solution:
    def find_set(self,node):
        if self.parent[node] == -1:
            return node
        
        return self.find_set(self.parent[node])
    
    def kruskals(self,edges,vertices):
        self.parent = [-1]*(vertices)
        ans = 0
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            
            lp_u = self.find_set(u)
            lp_v = self.find_set(v)
            
            if lp_u != lp_v:
                self.parent[lp_v] = lp_u
                ans += w
                
        return ans
        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
    
        v = len(points)
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                if i==j:
                    continue
                edges.append((i,j,abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
                
        #print(edges)
        edges.sort(key = lambda x:x[2])
        #print("Sorted : ",edges)
        
        return self.kruskals(edges,v)
        
            
        
