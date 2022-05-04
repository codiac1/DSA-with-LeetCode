# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,r,sr):
        if not r and not sr:
            return True
        
        if not r or not sr:
            return False
        
        return (r.val == sr.val) and self.check(r.left,sr.left) and self.check(r.right,sr.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        if not subRoot:
            return True
        
        return self.check(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
