def stock_buy_sell(list1):
    """try:
        max_so_far = list1[0]
        min_so_far = list1[0]
        for i in list1:
            if i > max_so_far:
                max_so_far = i
            if i < min_so_far:
                min_so_far = i
        return min_so_far , max_so_far
    except :
        pass
    """
    try:
        result = 0
        max_so_far = 0
        for i in range(len(list1)-1, -2 , -1):
            print("i" : i)
            if list1[i] > max_so_far:
                if list1[i] >= list1[i-1]:
                    max_so_far = list1[i]
                else:
                    max_so_far = list1[i-1]
        for j in list1:
            if max_so_far - j > result:
                result = max_so_far -j
                min1 = j
        return min1,result
    except:
        return -1

n = int(input("size of list :"))
input_list = [int(input()) for i in range(n)]
#{3 , 6, 5, 1, 4, 9,2, 6}
print("result : " , stock_buy_sell(input_list))