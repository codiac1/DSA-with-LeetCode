def twoStacks(maxSum, a, b):
    # Write your code here\
    sum1 = 0
    count =0
    a.reverse()
    b.reverse()
    while(sum1<=maxSum):
        if(sum1+a[-1]<=maxSum):
            sum1=sum1+a.pop() 
            count+=1
        if(sum1+b[-1]<=maxSum):
            sum1=sum1+b.pop() 
            count+=1
        else:
            break
    return count

a = [1,1, 0 ,0, 1, 0, 1,0, 0, 1, 0, 0, 1, 1, 1, 0, 0]
b = [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0 ,0 ,0 ,1 ,0 ,1]
max1 =  12
x = twoStacks(max1,a,b)
print(x)
