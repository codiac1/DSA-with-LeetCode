#Enter Python code here and hit the Run button.
class Solution:
    result = 0;
    
    def longestConsequetiveSequence(root):
        if not root:
            return 0
        getlongestSequence(root)
        return result
    
    def getlongestSequence(root):
        temp = 1;
        l = 0;
        r = 0;
        
        if root.left:
            if (root.left = root.val + 1):
                l = getlongestSequence(root.left)
                temp = max(temp , 1+l)
                
            if (root.right = root.val + 1):
                r = getlongestSequence(root.right)
                temp = max(temp , r+1)
        
        result = max(result , temp);
        return temp
        
        
        
