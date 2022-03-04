def highestValuePalindrome(s1, n, k):
    s = list(s1)
    if len(s) == 1:
        return "9"
    i = 0
    j = n-1
    change = [0]*n
    while(i<j):
        if s[i] == s[j]:
            pass
        else:
            m = max(s[i],s[j])
            if m==s[i]:
                s[j] = m
                change[j]=[1]
            else:
                s[i] = m
                change[i]=[1]
            k -= 1
        i += 1
        j -= 1
    if k<0:
        return '-1'
    else:
        i = 0
        j = n-1
        while(i<j and k>0):
            if s[i] != "9" and s[j] != "9":
                s[i] = s[j] = '9'
                if change[i] != 1:
                    k -= 1 
                if change[j] != 1:
                    k -= 1
            i += 1
            j -= 1
        s2 = "".join(s)
        return s2

s = "092282"
k = 3
print(highestValuePalindrome(s, 6, 3))
