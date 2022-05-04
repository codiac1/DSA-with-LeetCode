class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = {}
        for i in stones:
            if i not in d:
                d[i] = set()
        d[0].add(1)
        for k,v in d.items():
            for ele in v:
                nt = k+ele
                if nt in d:
                    d[nt].add(ele)
                    d[nt].add(ele+1)
                    if (ele-1)>0:
                        d[nt].add(ele-1)
        
        if len(d[stones[-1]]) ==0:
            return False
        else:
            return True
            
