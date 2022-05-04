class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [[0]*(n) for i in range(n)]
        max_rank = 0
        d = {}
        for r in roads:
            adj[r[0]][r[1]] = 1
            adj[r[1]][r[0]] = 1
        
        for i in range(len(adj)):
            d[i] = adj[i].count(1)
        
        for i in range(n):
            for j in range(i+1,n):
                temp = d[i] + d[j]
                if adj[i][j] == 1:
                    temp-=1
                #print(temp)
                if max_rank<temp:
                    max_rank = temp
        
        return max_rank
                
            
        
        
