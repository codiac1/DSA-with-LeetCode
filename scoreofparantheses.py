def scoreOfParentheses(s):
    stk = []
    for i in s:
        if (i == "("):
            stk.append(-1)
        else:
            if stk[-1] == -1:
                stk.pop()
                stk.append(1)
            else:
                sum1 = 0
                while (stk[-1] != -1):
                    sum1 += stk.pop()
                stk.pop()
                stk.append(2 * sum1)
    return sum(stk)

s = "(()(()))"
print(scoreOfParentheses(s))