# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructBST(self,preorder,low,high):
        
        if (self.index >= len(preorder)):
            return None
        
        if (preorder[self.index]<low or preorder[self.index]>high):
            return None
        
        root = TreeNode(preorder[self.index])
        self.index+=1
        root.left = self.constructBST(preorder,low,root.val)
        root.right = self.constructBST(preorder,root.val,high)
        
        return root
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        return self.constructBST(preorder,-math.inf,math.inf)
        
