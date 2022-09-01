class Pranav:
    def build_graph(self, edges , v):
        graph = {}
        for i in range(v):
            graph[i] = list()
        for edge in edges :
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
    
    def dfs(self, node, parent, graph, visited):
        visited[node] = True
        for nbr in graph[node]:
            if visited[nbr] is False:
                self.dfs(nbr, node , graph, visited)
            elif nbr != parent:
                print(nbr , "-->" , node)

    def print_backedge(self, v , e , edges):
        visited = [False]*v
        graph = self.build_graph(edges , v)
        #print(graph)
        self.dfs(0, -1, graph, visited)

if __name__ == "__main__":
    v = 7
    e = 7
    edges = [(0,1), (1,2), (1,3), (3,4), (3,6), (4,5), (5,6)]
    obj = Pranav()
    obj.print_backedge(v , e , edges)
