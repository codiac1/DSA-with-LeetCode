def isAlienSorted(words, order):
for i in range(len(words)-1):
        first = words[i]
        second = words[i+1]
        if dict1[second[0]]>dict1[first[0]]: continue
        elif first == second[:len(first)] and len(second)>len(first):continue
        elif len(second)<len(first) and second == first[:len(second)]:return False
        else:
            
            #O(20) -> O(1)
            for firstStrChar,SecondStrChar in zip(first,second):
                if dict1[firstStrChar]>dict1[SecondStrChar]:
                    return False
    return True
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))
