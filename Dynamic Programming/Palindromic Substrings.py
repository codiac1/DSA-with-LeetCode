class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        count = 0
        for gap in range(0,n):
            i = 0
            j = gap
            while(j<n):
                if gap == 0:
                    dp[i][j] = 1
                    count += 1
                    start = i
                    end = j
                elif gap ==1 :
                    if s[i]==s[j]:
                        dp[i][j] = 1
                        count += 1
                        start = i
                        end = j
                else:
                    if (s[i]==s[j] and dp[i+1][j-1]):
                        count += 1
                        dp[i][j] = 1 
                        start = i
                        end = j 
                i+=1
                j+=1
        return count
                     
