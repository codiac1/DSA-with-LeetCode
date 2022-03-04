def isAnagram(s, t) :
        if len(s)!=len(t):return False
        fmap = {}
        for i in s:
            fmap[i] = fmap.get(i,0)+1
        for j in t:
            if j in fmap:
                fmap[j] -=1
            else:
                return False
        print(fmap)
        for i in fmap:
            if fmap[i] !=0:
                flag = 5
        if flag==5:
            return False
        return True

s = input("1.")
t = input("2.")
print(isAnagram(s,t))
