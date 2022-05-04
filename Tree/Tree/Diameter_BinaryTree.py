# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_height(self,root):
        if (not root):
            return 0
        
        left_height = self.find_height(root.left)
        right_height = self.find_height(root.right)
        curr_diameter = left_height + right_height
        
        self.diameter = max(curr_diameter,self.diameter)
        
        return (max(left_height,right_height)+1)
        
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0
        self.find_height(root)
        return self.diameter
