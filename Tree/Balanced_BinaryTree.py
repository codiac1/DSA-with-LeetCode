# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_height(self,root):
        if not root:
            return 0
        
        left_h = 1 + self.find_height(root.left)
        right_h = 1 + self.find_height(root.right)
         
        if abs(left_h-right_h)>1:
            self.balanced = False
        
        return max(left_h,right_h)
        
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced=True
        if not root:
            return True
        if not root.left and not root.right:
            return True
        self.find_height(root)
        return self.balanced
        
