class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {}
        
        if stones[1] != 1:
            return False
        
        for ele in stones:
            dp[ele] = set()
            
        dp[0].add(1)
        
        for k ,s in dp.items():
            for v in s:
                next_pos = k + v
                 
                if next_pos not in dp:
                    continue
                
                if next_pos == stones[-1]:
                    return True
                
                if v-1 >= 1:  
                    dp[next_pos].add(v-1)
                
                dp[next_pos].update([v , v+1])
        
        return False
