# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_min(self,root):
        if not root:
            return -1
        
        if root.left:
            return self.find_min(root.left)
        else:
            #print(root)
            return root.val
        
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        
        else:
            if root.left and root.right:
                right_min = self.find_min(root.right)
                root.val = right_min
                root.right = self.deleteNode(root.right,right_min)
                return root
                
            elif not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            else:
                return None
            
        return root
                
        
            
            

            
            
        
        
        
