class Solution:
    def find_coordinates(self,curr,n):
        row = n-1 - ((curr-1)//n)
        col = (curr-1) % n
        if row%2 == n%2 :
            return (row,(n-1)-col)
        else:
            return (row,col)
    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        min_step = 0
        n = len(board)
        visited = [[(False) for i in range(n)] for j in range(n)]
        start = 1
        end = n*n
        
        queue = deque()
        visited[n-1][0] = True
        queue.append(start)
        
        while(queue):
            l = len(queue)
            for i in range(l):
                curr = queue.popleft()
                
                if curr == end:
                    return min_step
                
                for dice in range(1,7):
                    if curr+dice > end:
                        break
                    
                    next_row,next_col = self.find_coordinates(curr + dice,n)
                    if not visited[next_row][next_col] :
                        visited[next_row][next_col] = True
                        if board[next_row][next_col] != -1:
                            queue.append(board[next_row][next_col])
                        else:
                            queue.append(curr + dice)
                        
            min_step += 1
                   
        return -1
        
