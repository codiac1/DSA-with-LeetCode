from heapq import *

class Prims_algo:
    def distance(self , points , x1 , y1 , x2 , y2): # this distance formula will vary from question to question 
        return abs(x1 - x2) + abs(y1 - y2);

    def MinimumCostTree(self,points): # template
        n = len(points);
        min_heap = [];  # to get minimum cost wala node every time
        visited = set();

        cost = 0 ;
        x , y = points[0];
        heappush(min_heap , (0 ,(x , y)));

        while(min_heap and len(visited) < len(points)): # checking length to avoid any cycle
            dist, curr = heappop(min_heap); 
            
            if curr in visited:
                continue;
            cost += dist;
            visited.add(curr);

            for point in points :
                if (point[0] , point[1]) in visited : # try all points now
                    continue;
                new_dist = self.distance(points , curr[0] , curr[1], point[0], point[1]);

                heappush(min_heap , (new_dist ,(point[0] , point[1])));

        return cost;

mst = Prims_algo();

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
min_cost = mst.MinimumCostTree(points);
print(min_cost);

points = [[3,12],[-2,5],[-4,1]]
min_cost = mst.MinimumCostTree(points);
print(min_cost);


            
            
