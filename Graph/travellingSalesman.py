import math

def TSP(cities, visited, city, n,dp):
    #Base Condition
    if visited == ((1<<n)-1):
        return cities[city][0]

    if dp[visited][city] != -1:
        return dp[visited][city]

    cost = math.inf

    for choice in range(0,n):
        if (visited & (1<<choice)) == 0:
            temp = cities[city][choice] + TSP(cities,(visited | (1<<choice)),choice,n,dp)
            cost = min(temp,cost)

    dp[visited][choice] = cost
    return dp[visited][choice]

cities = [[0,20,42,25],[20,0,30,34],[42,30,0,10],[25,34,10,0]]
v = 4
dp = [[(-1)for i in range(v)] for j in range(1<<v)]
print(TSP(cities,1,0,v,dp))
