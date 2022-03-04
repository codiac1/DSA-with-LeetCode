<<<<<<< HEAD
def binexponentiation(a,b):
    while(b>0):
        res = binexponentiation(a,b//2)
        if(b&1):
            return a*res*res
        return res*res
    if(b==0):
        return 1

a  = int(input())
b  = int(input())
print(binexponentiation(a,b))
=======
def binexponentiation(a,b):
    while(b>0):
        res = binexponentiation(a,b//2)
        if(b&1):
            return a*res*res
        return res*res
    if(b==0):
        return 1

a  = int(input())
b  = int(input())
print(binexponentiation(a,b))
>>>>>>> 7dbfc6ee8456b4bdf53b3d0eaa07fbfbb6d7917a
