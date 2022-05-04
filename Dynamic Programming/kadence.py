import math
class Pranav:
    def kadence(self, arr):
        n = len(arr)
        sub_arr_sum = 0
        max_sum = arr[0]
        for i in range(n):
            sub_arr_sum = sub_arr_sum + arr[i]
            if sub_arr_sum <0:
                sub_arr_sum = 0
            elif( sub_arr_sum > max_sum):
                max_sum = sub_arr_sum
        return max_sum

obj = Pranav()
arr = [-2,-3,4,-2,-1,1,5,-3]
ans = obj.kadence(arr)
print(ans)
