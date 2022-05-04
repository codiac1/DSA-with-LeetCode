class Solution:
    def build_graph(self,times,n):
        graph = {}
        for i in range(1,n+1):
            graph[i] = list()
        
        for time in times:
            graph[time[0]].append(time[1])
            
        return graph
            
    def build_cost(self,times):
        cost = {}
        for time in times:
            cost[(time[0],time[1])] = time[2]
            
        return cost
    
    def networkDelayTime(self, times: List[List[int]], n: int, src: int) -> int:
        
        distance = [math.inf]*(n+1)
        parent = [-1]*(n+1)
        visited = [False]*(n+1)
        
        graph = self.build_graph(times,n)
        cost = self.build_cost(times)
        
        min_heap = []
        
        heappush(min_heap,(0,src))
        distance[src] = 0
        
        while(min_heap):
            curr_distance,curr_node = heappop(min_heap)
            
            if visited[curr_node] is False:
                visited[curr_node] = True
                for nbr in graph[curr_node]:
                    if distance[curr_node] + cost[(curr_node,nbr)] < distance[nbr]:
                        distance[nbr] = distance[curr_node] + cost[(curr_node,nbr)]
                        heappush(min_heap,(distance[nbr],nbr))
                        parent[nbr] = curr_node
        
        maxtime = -math.inf
        for i in range(1,n+1):
            if distance[i] == math.inf:
                return -1
            else:
                maxtime = max(maxtime,distance[i])
                
        return maxtime
        
