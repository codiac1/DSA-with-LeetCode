def insert( intervals, newInterval) :
    ans = []
    i=0
    while(i < len(intervals) and intervals[i][1] < newInterval[0] ):
        ans.append(intervals[i])
        i+=1
    while(i <len(intervals) and intervals[i][0] <= newInterval[1] ):
        min1 = min(intervals[i][0], newInterval[0])
        max1 = max(intervals[i][1] ,newInterval[1])
        newInterval[0] = min1
        newInterval[1] = max1
        i+=1
    ans.append(newInterval)
    while(i<len(intervals)):
        ans.append(intervals[i])
        i+=1
    return ans
inputarr=[[1,2] , [3,4] , [6,7],[8,10], [10,12]]
new = [5,8]
print(insert( inputarr, new))