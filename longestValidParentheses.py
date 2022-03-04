def longestValidParentheses(s):
    stk = [-1]
    maxlen = 0
    for i in range(len(s)):
        if s[i] == '(':
            stk.append(i)
        else:
            stk.pop()
            if len(stk) == 0:
                stk.append(i)
            else:
                maxlen = max(maxlen, i - stk[-1])
    return maxlen
print(longestValidParentheses(")()())"))

