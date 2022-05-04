# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        queue=deque()
        queue.append(root)
        count=0
        while(queue):
            
            level=len(queue)
            l=[]
            for i in range(level):
                x=queue.popleft()
                l.append(x.val)
                
                if x.left:
                    queue.append(x.left)
                    
                if x.right:
                    queue.append(x.right)
            
            count+=1
        
        return count
            
                    
            
            
