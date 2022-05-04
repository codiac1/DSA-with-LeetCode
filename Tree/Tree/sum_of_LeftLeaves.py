# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if not root:
            return
        
        if root.left and not root.left.left and not root.left.right:
            self.x += root.left.val
            
        if root.left:
            self.solve(root.left)
            
        if root.right:
            self.solve(root.right)
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.x = 0
        self.solve(root)
        
        return self.x
        
