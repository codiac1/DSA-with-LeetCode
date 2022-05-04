# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,path,target):

        if not root.left and not root.right and root.val==target:
            self.ans.append(path)
        
        path.append(root.val)
        if root.left:
            left = path[:]
            self.dfs(root.left,left,(target-root.val))
                      
        if root.right:
            right = path[:]
            self.dfs(root.right,right,(target-root.val))
                
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        
        path = []
        if not root:
            return []
        
        self.dfs(root,path,targetSum)
        
        return self.ans
        
        
