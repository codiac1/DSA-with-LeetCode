class Solution:
    def dfs(self,mat,x,y,row,col,newcolor,visited):
        visited[x][y] = True
        oldColor = mat[x][y]
        mat[x][y] = newcolor 
        
        
        if x-1>= 0 and mat[x-1][y] == oldColor and visited[x-1][y] is False:
            self.dfs(mat,x-1,y,row,col,newcolor,visited)
        if x+1< len(mat) and mat[x+1][y] == oldColor and visited[x+1][y] is False:
            self.dfs(mat,x+1,y,row,col,newcolor,visited)
        if y-1>= 0 and mat[x][y-1] == oldColor and visited[x][y-1] is False:
            self.dfs(mat,x,y-1,row,col,newcolor,visited)
        if y+1<len(mat[0]) and mat[x][y+1] == oldColor and visited[x][y+1] is False:
            self.dfs(mat,x,y+1,row,col,newcolor,visited)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newcolor: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        
        visited = [[False for i in range(col)] for j in range(row)]
        
        self.dfs(image,sr,sc,row,col,newcolor,visited)
        return image
        
        
        
