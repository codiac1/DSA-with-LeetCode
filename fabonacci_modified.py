inp = input().split(" ")
t =[]
t.append(int(inp[0]))
t.append(int(inp[1]))
n = int(inp[2])
for i in range(2,n):
    t[i] = t[i-2] +(t[i-1]**2)
print(t[-1])
