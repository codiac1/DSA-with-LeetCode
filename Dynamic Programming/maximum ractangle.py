class Solution:
    def histogram(self, arr):
        n = len(arr)
        left = []
        right = []
        stk = []
        
        for i in range(n):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            if not stk:
                left.append(-1)
            elif arr[stk[-1]] < arr[i]:
                left.append(stk[-1])
            stk.append(i)
        stk.clear()
        
        for i in range(n-1,-1,-1):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            if not stk:
                right.append(n)
            elif arr[stk[-1]] < arr[i]:
                right.append(stk[-1])
            stk.append(i)
        right.reverse()
        maxarea = 0
        for i in range(n):
            area = (right[i]-left[i]-1)*arr[i]
            if maxarea <= area:
                maxarea = area
        
        return maxarea
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        maxarea = 0
        
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
                
        for rownum in range(rows):
            if rownum == 0:
                area = self.histogram(matrix[0])
            else:
                for c in range(cols):
                    if matrix[rownum][c] != 0 :
                        matrix[rownum][c] += matrix[rownum-1][c]
                
                area = self.histogram(matrix[rownum])
            if area >= maxarea:
                maxarea = area
        return maxarea

                
            
        
        
