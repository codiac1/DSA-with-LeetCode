from collections import *
class Solution:
    def build_graph(self, flights,n):
        for i in range(n):
            self.graph[i] = []
            
        for flight in flights:
            self.graph[flight[0]].append(flight[1])
            self.time[(flight[0],flight[1])] = flight[2]
        
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dist: int, k: int) -> int:
        distance = [math.inf]*(n)
        stops = [0]*(n)
        self.graph = {}
        self.time = {}
        distance[src] = 0
        self.build_graph(flights, n)
        min_heap = []
        heappush(min_heap ,(distance[src],src,stops[src]))
        
        while(min_heap):
            curr_dist,curr_node,curr_stop = heappop(min_heap)
            if curr_node == dist:
                return curr_dist
            if curr_stop > k:
                continue
            
            for nbr in self.graph[curr_node]:
                if curr_dist+self.time[curr_node,nbr]< distance[nbr]:
                    distance[nbr] = curr_dist+self.time[curr_node,nbr]
                    stops[nbr] = curr_stop +1
                    heappush(min_heap ,(distance[nbr], nbr , stops[nbr]))
                elif curr_stop+1 < stops[nbr]:
                    heappush(min_heap,(curr_dist+self.time[curr_node,nbr], nbr ,curr_stop + 1))
        return -1
        
        
