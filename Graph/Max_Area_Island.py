class Solution:
    def dfs(self,x,y,visited,grid):
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or (x,y) in visited or grid[x][y] == 0:
            return 0
        visited.add((x,y))
        
        return 1 + self.dfs(x+1,y,visited,grid) + self.dfs(x-1,y,visited,grid) + self.dfs(x,y-1,visited,grid) + self.dfs(x,y+1,visited,grid)
        
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        x = 0
        for arr in grid:
            x += arr.count(1)
            
        if x==0:
            return 0
        
        max_area = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area= max(max_area,self.dfs(i,j,visited,grid))
                    
        return max_area
                    
        
        
