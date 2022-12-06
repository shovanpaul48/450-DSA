# https://www.youtube.com/watch?v=w_KEocd__20

# Maximum Sub array sum 
# complexity : O(n)


def KadensAlgoWithK(a,key):
    l = len(a)
    start,sum,maxlen= 0 ,0,0
    end = -1
    while (start < l) :
        while ((end + 1 < l) and (sum + a[end + 1] <= key)) :
            sum += a[end + 1]

        if (sum == key):
            maxLength = max(maxLength, (end - start + 1))

        sum -= a[start]
        start += 1
    
    return maxlen

# KadensAlgo([-13 ,0 ,6 ,15 ,16 ,2 ,15, -12 ,17 ,-16 ,0, -3, 19, -3, 2 ,-9, -6])
print(KadensAlgoWithK([-2,-3,0,-9,4,-1,-2,1,5,-3],0))
        


