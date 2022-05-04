# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,min_,max_):
        if not root:
            return True
        
        if root.val > min_ and root.val < max_ :
            return self.check(root.left,min_,root.val) and self.check(root.right,root.val,max_)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.check(root, -math.inf , math.inf)
        
