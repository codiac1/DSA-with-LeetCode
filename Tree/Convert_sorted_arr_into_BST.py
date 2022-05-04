# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,low,high,arr):
        if low<=high:
            mid = (low+high)//2
            return TreeNode(arr[mid], self.build(low,mid-1,arr), self.build(mid+1,high,arr))
        return None
        
    
    def sortedArrayToBST(self, arr: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        if(len(arr)==0):
            return root
        
        if(len(arr) == 1):
            root.val = arr[0]
            return root
        
        if(len(arr) == 2):
            root.val = arr[-1]
            root.left = TreeNode(arr[0])
            
            return root
        
        n = len(arr)
        return self.build(0,n-1,arr)
        
        
        
            
        
        
            
