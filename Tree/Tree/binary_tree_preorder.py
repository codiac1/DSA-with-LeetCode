# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def display(self,root,ans):
        if not root:
            return 
        
        ans.append(root.val)
        if root.left:
            self.display(root.left,ans)
            
        if root.right:
            self.display(root.right,ans)   
        
        return ans
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        return self.display(root,ans)
