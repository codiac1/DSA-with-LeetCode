class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dig_set = set()
        for sublist in dig:
            dig_set.add(tuple(sublist))
        count = 0
        for afact in artifacts:
            r1, c1 ,r2 ,c2 = afact
            flag = 0
            for i in range(r1 ,r2+1):
                for j in range(c1, c2+1):
                    if (i,j) not in dig_set:
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                count += 1
        return count 
                    
