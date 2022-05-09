# Topic :: Articulation Points and Bridges ::  
# In this question basically we need to find all the bridges present in a graph

class Solution:
    def build_graph(self, connections,n):
        graph = {}
        # using a adjecency list representation
        for i in range(n):
            graph[i] = list()
            
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
    
    def dfs(self, node, parent, graph, timer):
        self.visited[node] = True
        self.discovered_time[node] = timer
        self.lowest_time[node] = timer
        timer += 1
        
        for nbr in graph[node]:
            if nbr == parent :
                continue
                
            elif self.visited[nbr] is False:
                self.dfs(nbr, node, graph, timer)
                self.lowest_time[node] = min(self.lowest_time[node] , self.lowest_time[nbr])
                
                # main condition :: if low_time[child] > disc_time[parent] then that edge is bridge
                
                if self.lowest_time[nbr] > self.discovered_time[node]:
                    self.bridges.append([node,nbr])
           
            else:  # means a backedge is present 
                self.lowest_time[node] = min(self.lowest_time[node] , self.discovered_time[nbr])
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.visited = [False]*n
        self.discovered_time = [0]*n
        self.lowest_time = [0]*n
        self.bridges = []
        
        graph = self.build_graph(connections,n)
        timer = 0
        
        for vertex in range(n):
            if self.visited[vertex] is False:
                self.dfs(vertex ,-1 , graph , timer)
        
        return self.bridges
    
