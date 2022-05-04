# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root):
        if not root:
            return
        
        if root.val>=self.low and root.val<=self.high:
            self.sum += root.val
            self.dfs(root.left)
            self.dfs(root.right)
            
        if root.val>self.low and root.val>self.high:
            self.dfs(root.left)
            
        if root.val<self.low and root.val<self.high:  
            self.dfs(root.right)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        self.sum = 0
        
        self.dfs(root)   
        
        return self.sum
        
