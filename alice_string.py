<<<<<<< HEAD
def samestring(str1,str2):
    n = len(str1)
    for i in range(n):
        if(str1[i]==str2[i]):
            continue
        else:
            index = i
            break

    prefix = str1[:index+1]
    prefix_1=" "
    for i in range(len(prefix)):
        prefix_1 += chr(ord(prefix[i])+1)

    prefix_1 = prefix_1 + str1[index:]
    if(prefix_1 == str2):
        return "YES"
    else:
        return samestring(prefix_1,str2)
    
str1=input()
str2=input()
samestring(str1,str2)
=======
def samestring(str1,str2):
    n = len(str1)
    for i in range(n):
        if(str1[i]==str2[i]):
            continue
        else:
            index = i
            break

    prefix = str1[:index+1]
    prefix_1=" "
    for i in range(len(prefix)):
        prefix_1 += chr(ord(prefix[i])+1)

    prefix_1 = prefix_1 + str1[index:]
    if(prefix_1 == str2):
        return "YES"
    else:
        return samestring(prefix_1,str2)
    
str1=input()
str2=input()
samestring(str1,str2)
>>>>>>> 7dbfc6ee8456b4bdf53b3d0eaa07fbfbb6d7917a
