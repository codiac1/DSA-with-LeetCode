# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self,total_sum ,min_val,max_val):
        self.total = total_sum
        self.max_val = max_val
        self.min_val = min_val
        
class Solution:
    def solve(self , root):
        if not root :
            return Node(0, math.inf , -math.inf)
        left_node = self.solve(root.left)
        right_node = self.solve(root.right)
        
        if not left_node or not right_node:
            return None
        if root.val <= left_node.max_val or root.val >= right_node.min_val:
            return None
        curr_sum = root.val+ left_node.total +  right_node.total
        self.max_sum = max(self.max_sum, curr_sum)
        
        return Node(curr_sum , min(root.val,left_node.min_val), max(root.val, right_node.max_val))
                
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.max_sum = 0
        self.solve(root)
        return self.max_sum
