from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        d = {}
        for i in range(len(routes)):
            for bus_stop in routes[i]:
                if bus_stop not in d:
                    d[bus_stop] = [i]
                else:
                    d[bus_stop].append(i)
                    
        #print(d)
        
        queue = deque()
        visited_bus = set()
        visited_stop = set()
        
        queue.append(source)
        visited_stop.add(source)
        level = 0
        
        while(queue):
            l = len(queue)
            for i in range(l):
                curr = queue.popleft()
                if curr == target:
                    return level
                buses = d[curr]
                for bus in buses:
                    if bus not in visited_bus:
                        for bus_stop in routes[bus]:
                            if bus_stop not in visited_stop:
                                queue.append(bus_stop)
                                visited_stop.add(bus_stop)
                    visited_bus.add(bus)
                    
            level += 1
        
        return -1
                
        
                    
                    
