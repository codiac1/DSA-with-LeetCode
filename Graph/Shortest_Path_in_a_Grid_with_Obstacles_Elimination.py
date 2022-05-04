class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        steps = 0
        
        queue.append((0,0,k,steps))
        
        visited = set()
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        if grid[-1][-1]==1 and k>0:
            k-=1
        
        while(queue):
            x,y,k,steps = queue.popleft()
            if (x,y,k) in visited:
                continue
            visited.add((x,y,k))
            
            if (x==row-1) and (y==col-1):
                return steps
            
            for u,v in direction:
                nx = u + x
                ny = v + y
                
                if (0<=nx<row) and (0<=ny<col):
                    if not grid[nx][ny]:
                        queue.append((nx,ny,k,steps+1))
                
                    elif k:
                        queue.append((nx,ny,k-1,steps+1))        
        return -1
