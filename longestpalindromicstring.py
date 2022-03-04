def longestPalindrome(s):
    n = len(s)
    dp = [[None]*(n+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][i] = 1
    for i in range(n+1):
        if i +1 ==n:
            break
        if s[i-1] ==s[i]:
            dp[i-1][i] = 1
        else:
            dp[i-1][i] = 0
    for row in dp:
        print(row)

s= "ABBABC"
print(longestPalindrome(s))
