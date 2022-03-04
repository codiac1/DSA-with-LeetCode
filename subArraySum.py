def subArraySum(arr, n, s): 
        i=0
        j=0
        sum1=0
        list1 =[]
        while(j<n):
            if sum1 <s :
                sum1 = sum1 +arr[j]
                j += 1
            elif sum1>s :
                sum1 = sum1 - arr[i]
                i += 1
            elif sum1 ==s :
                list1.append(i+1)
                list1.append(j)
                break
            else:
                pass
        if len(list1)>0:
            return list1    
        else:
            list1.append(-1)
            return list1

arr= [135,101,170,125,79,159,163,65,106,146,82,28,162,92,196,143,28,37,192,5,103,154,93,183,22,117,119,96,48,127,172,139,70,113,68,100,36,95,104,12,123,134]
ans = subArraySum(arr, 42, 468)
for i in ans :
    print(i)
