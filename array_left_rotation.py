<<<<<<< HEAD
n = input()
n= n.split(" ")
n1 = int(n[0])
d = int(n[1])

l1 = list(map(int,input().split(" ")))

while(d!=0):
    x = l1.pop(0)
    l1.append(x)
    d-=1
for i in l1:
    print(i,end=" ")
=======
n = input()
n= n.split(" ")
n1 = int(n[0])
d = int(n[1])

l1 = list(map(int,input().split(" ")))

while(d!=0):
    x = l1.pop(0)
    l1.append(x)
    d-=1
for i in l1:
    print(i,end=" ")
>>>>>>> 7dbfc6ee8456b4bdf53b3d0eaa07fbfbb6d7917a
