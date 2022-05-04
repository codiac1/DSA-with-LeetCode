# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mirror(self,p,q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if (p.val==q.val) and self.mirror(p.left,q.left) and  self.mirror(p.right,q.right):
            return True
    '''def inorder(self, root,ans):
        
        if not root:
            return 
        
        if root.left:
            self.inorder(root.left,ans)
        ans.append(root.val)
        if root.right:
            self.inorder(root.right,ans)
        
        return ans'''
    
    
        
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
         return self.mirror(p,q)
        
        
