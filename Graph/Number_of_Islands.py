class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        island = 0
        
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    grid[i][j] = "*"
                    q.append((i,j))
                    
                    island += 1
                    while(q):
                        x,y = q.popleft()
                        for k,v in direction:
                            nx = k+x
                            ny = v+y
                            if (0<=nx<rows) and (0<=ny<cols):
                                if grid[nx][ny] == "1":
                                    grid[nx][ny] = "*"
                                    q.append((nx,ny))
        return island
                      
                
                
                    
