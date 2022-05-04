class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
        if end not in wordSet:
            return 0
        
        if begin in wordSet:
            wordSet.remove(begin)
        
        queue = deque()
        count=0
        queue.append(begin)
        
        while(queue):
            count+=1
            level = len(queue)
            
            for i in range(level):
                curr_word = queue.popleft()
                for j in range(len(curr_word)):
                    for x in ascii_lowercase:
                        temp = curr_word[:j] + x + curr_word[j+1:]
                        
                        if temp in wordSet:
                            queue.append(temp)
                            if temp == end:
                                return (count+1)
                            wordSet.remove(temp)
        return 0
                
            
            
