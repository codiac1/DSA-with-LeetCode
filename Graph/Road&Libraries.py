def build_graph(cities , n):
    d = {}
    for i in range(1,n+1):
        d[i] = list()
        
    for city in cities:
        d[city[0]].append(city[1])
        d[city[1]].append(city[0])
    
    return d

def dfs(graph, vertex, visited , node_count):
    visited[vertex] = True
    node_count += 1
        
    for nbr in graph[vertex]:
        if visited[nbr] is False:
            node_count = dfs(graph, nbr, visited , node_count)  
    
    return node_count
        
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road>c_lib:
        return n*c_lib
    
    graph = build_graph(cities , n)
    
    visited = [False]*(n+1)
    l = []
    components = 0 
    
    for vertex in range(1,n+1):
        if visited[vertex] is False:
            node_count = 0
            nodes = dfs(graph , vertex , visited , node_count)
            components += 1
            l.append(nodes)
    #print(l)
    total = 0
    for i in l:
        total = total + (c_road*(i-1))

    total = total + (components*c_lib)

    return total

if __name__ == "__main__":
  num_cities = int(input())
  c_lib = int(input())
  c_road = int(input())
  cities = []

  for _ in range(m):
    cities.append(list(map(int, input().rstrip().split())))
  print(roadsAndLibraries(num_cities, c_lib, c_road, cities))
  
