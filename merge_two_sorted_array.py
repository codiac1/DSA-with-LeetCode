def next_gap(gap):
    if gap > 1:
        gap = (gap // 2) + (gap % 2)
        return gap
    else:
        return 0
# approach 1
def merge_1(arr1, arr2, n, m):
    gap = n + m
    #gap = next_gap(gap)
    while gap > 0:
        if gap > 1:
            gap = (gap // 2) + (gap % 2)
        else:
            gap =0
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[gap + i]:
                arr1[i], arr1[gap + i] = arr1[i + gap], arr1[i]
            i += 1
        if gap > n:
            j = gap - n
        else:
            j = 0
        while j < m and i < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        if j < m:
            j = 0
        while j + gap < m:
            if arr2[j] > arr2[gap + j]:
                arr2[j], arr2[gap + j] = arr2[j + gap], arr2[j]
            j += 1
        if gap > 1:
            gap = (gap // 2) + (gap % 2)
        #else:
        #    gap =0

# approach 2
def merge_2(arr1, arr2, n, m):
    gap = n + m
    gap = next_gap(gap)
    while gap > 0:
        i = 0
        while (i + gap < n):
            if (arr1[i] > arr1[i + gap]):
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1
        if (gap > n):
            j = gap - n
        else:
            j = 0

        while (j < m and i < n):
            if (arr1[i] > arr2[j]):
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        if (j < m):
            j = 0
        while (j + gap < m):
            if (arr2[j] > arr2[j + gap]):
                arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
            j += 1
        gap = next_gap(gap)

arr1 = [1, 3, 4, 6, 7]
arr2 = [2, 5, 10]
merge_1(arr1, arr2, len(arr1), len(arr2))
print(arr1)
print(arr2)
