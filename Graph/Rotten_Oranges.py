class Node:
    def __init__(self,x,y,time):
        self.x=x
        self.y=y
        self.time=time

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row=len(grid)
        cols=len(grid[0])
        queue = deque()
        
        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 2:
                    node = Node(i,j,0)
                    queue.append(node)
        ans=0
        while(queue):
            
            curr_node = queue.popleft()
            x=curr_node.x
            y=curr_node.y
            time=curr_node.time
            
            if x-1>=0 and grid[x-1][y]==1:
                grid[x-1][y] = 2
                node=Node(x-1,y,time+1)
                queue.append(node)
                ans=time+1
                
            if x+1<row and grid[x+1][y]==1:
                grid[x+1][y] = 2
                node=Node(x+1,y,time+1)
                queue.append(node)
                ans=time+1
                
            if y-1>=0 and grid[x][y-1]==1:
                grid[x][y-1] = 2
                node=Node(x,y-1,time+1)
                queue.append(node)
                ans=time+1
                
            if y+1<cols and grid[x][y+1]==1:
                grid[x][y+1] = 2
                node=Node(x,y+1,time+1)
                queue.append(node)
                ans=time+1
                
        
        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
                
        return ans
                    
            
                    
