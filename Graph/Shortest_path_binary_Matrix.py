class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        direction = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
        
        if grid[0][0]==1 or grid[rows-1][cols-1]==1:
            return -1
        
        queue = deque()
        queue.append((0,0,1))
        grid[0][0] = 1
        
        while(queue):
            row,col,d = queue.popleft()
            if row==rows-1 and col==cols-1:
                return d
            for u,v in direction:
                x = row + u
                y = col + v
                
                if x<0 or x>=rows or y<0 or y>=cols or grid[x][y] == 1:
                    continue
                    
                queue.append((x,y,d+1))
                grid[x][y] = 1
        
        return -1
            
        
