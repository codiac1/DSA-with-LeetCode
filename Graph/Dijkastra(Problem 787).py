class Solution:
    def build_graph(self,flights,n):
        for i in range(n):
            self.graph[i] = list()
            
        for flight in flights:
            self.graph[flight[0]].append(flight[1])
            self.cost[(flight[0],flight[1])] = flight[2]
            
        #print(self.graph)
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [math.inf]*(n)
        stop = [0]*(n)
        self.graph = {}
        self.cost = {}
        
        distance[src] = 0
        self.build_graph(flights,n)
        min_heap = []
        heappush(min_heap,(0,src,0))
        
        while(min_heap):
            curr_dist,curr_node, curr_stop = heappop(min_heap)
            
            if curr_node == dst:
                return curr_dist
            
            if curr_stop > k:
                continue
            
            for nbr in self.graph[curr_node]:
                #print(nbr,price)
                
                if curr_dist + self.cost[curr_node,nbr] < distance[nbr]:
                    distance[nbr] = curr_dist + self.cost[curr_node,nbr]
                    stop[nbr] = curr_stop+1
                    #print(next_dist,distance[nbr],stop[nbr])
                    heappush(min_heap, (distance[nbr],nbr,stop[nbr]))
                    #print(min_heap) 
                       
                elif curr_stop+1 < stop[nbr] :
                    heappush(min_heap,(curr_dist + self.cost[curr_node,nbr],nbr,curr_stop+1))
            
        return -1
                        
                        
            
        
        
        
