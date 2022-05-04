import math
class House:
    def build_graph(self,n,well,pipes):
        self.graph = {}
        self.cost = {}

        for i in range(n):
            self.graph[i] = list()

        for i in range(n):
            self.cost[(0,i+1)] = well[i]
            self.graph[0].append(i+1)

        for pipe in pipes:
            parent = pipe[0]
            child = pipe[1]
            cost = pipe[2]
            self.graph[parent].append(child)
            self.cost[(parent,child)] = cost

        print(self.graph)
        print(self.cost)

    def find_min(self,distance,visited):
        min_val = math.inf
        index = -1

        for i in range(len(distance)):
            if visited[i] == False and distance[i] < min_val:
                min_val = distance[i]
                index = i
        return index
            
    def prims(self,n,wells,pipes):
        distance = [math.inf]*(n+1)
        visited = [False]*(n+1)
        distance[0] = 0
        for vertex in range(n+1):
            curr_node = self.find_min(distance,visited)
            visited[curr_node] = True
            
        return None
    
    def min_dist_cost(self,n,well,pipes):
        graph = self.build_graph(n,well,pipes)
        return (self.prims(n,well,pipes))
        

well = [1,2,2]
pipes = [[1,2,1],[2,3,1]]
obj = House()
print(obj.min_dist_cost(3,well,pipes))
