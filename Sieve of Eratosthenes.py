rangeof = int(input("enter the limit :"))
l1 = [1]*(rangeof+1)
l1[0] = 0
l1[1] = 0
i = 2
while(i*i <= len(l1)):
    if(l1[i]==1):
        for j in range(i*i , len(l1), i):
            l1[j] = 0
    i+=1
for i in range(len(l1)):
    if(l1[i]==1):
        print(i)
