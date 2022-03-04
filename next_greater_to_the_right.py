def nextLargerElement(arr, n):
    ans = []
    stk = []
    for i in range(n - 1, -1, -1):
        while (len(stk) != 0 and stk[-1] <= arr[i]):
            stk.pop()
        if len(stk) == 0:
            ans.append(-1)
        # elif(stk[-1] > arr[i]):
        else:
            ans.append(stk[-1])
        stk.append(arr[i])

    ans.reverse()
    return ans