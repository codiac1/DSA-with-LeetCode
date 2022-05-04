# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        queue=deque()
        queue.append(root)
        count=0
        while(queue):
            l=len(queue)
            count+=1
            for i in range(l):
                x=queue.popleft()
                
                if not x.left and not x.right:
                    return count
                
                if x.left:
                    queue.append(x.left)
                    
                if x.right:
                    queue.append(x.right)
                    
                    
            
