# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans=[]
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        
        while(queue):
            level=len(queue)
            for _ in range(level):
                x=queue.popleft()
                if x.left :
                    queue.append(x.left)
                    
                if x.right :
                    queue.append(x.right)
            ans.append(x.val)
        
        return ans
                
                
        
