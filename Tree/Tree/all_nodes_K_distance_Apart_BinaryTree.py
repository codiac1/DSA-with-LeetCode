# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def build_dict(self,root):
        if not root:
            return
        if root.left:
            self.d[root.left.val] = root
            self.build_dict(root.left)
        
        if root.right:
            self.d[root.right.val] = root
            self.build_dict(root.right)
            
        
    def solve(self,target,k):
        queue = deque()
        visited = set()
        
        queue.append(target)
        while(queue) and k>0:
    
            l = len(queue)
            k-=1
            for i in range(l):
                curr = queue.popleft()
                visited.add(curr)
                  
                if curr.left and curr.left not in visited:
                    queue.append(curr.left)
        
                if curr.right and curr.right not in visited:
                    queue.append(curr.right)
            
                if self.d[curr.val] and self.d[curr.val] not in visited:
                    queue.append(self.d[curr.val])
                
        for i in queue:
            self.ans.append(i.val)
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return
        self.d = {}
        self.d[root.val] = None
        self.build_dict(root)

        #print(self.d)
        if k>len(self.d):
            return []
        
        self.ans = []
        self.solve(target,k)
        return self.ans
        
