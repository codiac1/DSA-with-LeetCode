def largestRectangleArea(ht):
    right = []
    left = []
    stk1 = []
    stk2 = []
    maxarea = 0

    for i in range(len(ht)):
        while (len(stk1) != 0 and stk1[-1][0] >= ht[i]):
            stk1.pop()
        if len(stk1) == 0:
            left.append(0)
        else:
            left.append(stk1[-1][1])
        stk1.append([ht[i], i])

    for i in range(len(ht) - 1, -1, -1):
        while (len(stk2) != 0 and stk2[-1][0] >= ht[i]):
            stk2.pop()
        if len(stk2) == 0:
            right.append(len(ht) + 1)
        else:
            right.append(stk2[-1][1])
        stk2.append([ht[i], i])
    print("left :" , left)
    print("right :" , right)
    for i in range(len(left)):
        w = left[i] - right[i] - 1
        area = w * ht[i]
        if area > maxarea:
            maxarea = area
    return maxarea

ht = [6,2,5,4,5,1,6]
print(largestRectangleArea(ht))