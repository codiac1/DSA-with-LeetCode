def romanToInt(s):
    num = 0
    d = {}
    list1 = ['I', 'V', 'X', 'L', 'C', 'D', 'M', "IV" , "IX", "XL", "XC"]
    list2 = [1, 5, 10, 50, 100 , 500, 1000 , 4 , 9, 40 , 90]

    for i in range(len(list1)):
        d[list1[i]] = list2[i]
    print(d)
    i =0
    while(i<len(s)):
        if i+1 < len(s) and s[i] == "I" and s[i+1] == "V":
            num += d[s[i]+s[i+1]]
            i +=1
            print("andr" ,num)
        elif i+1 < len(s) and s[i] == "I" and s[i+1] == "X":
            num += d[s[i]+s[i+1]]
            i +=1
            print("bahar" , num)
        elif i+1 < len(s) and s[i] == "X" and s[i+1] == "L":
                num += d[s[i]+s[i+1]]
                i +=1
        elif i+1 < len(s) and s[i] == "X" and s[i+1] == "C":
                num += d[s[i]+s[i+1]]
                i +=1
        else:
            num += d[s[i]]
            print("last" , num)
        i+=1
    return num

s= "MCMXCIV"
print(romanToInt(s))
