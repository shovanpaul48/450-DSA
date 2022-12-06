# https://www.youtube.com/watch?v=w_KEocd__20

# Maximum Sub array sum 
# complexity : O(n)


def KadensAlgo(a,key):
    l = len(a)
    j,sum,maximum = 0 ,0,0
    for i in range (l):
        sum = sum  + a[i]
        
        if sum < 0:
            sum = 0
            j = i +1

        elif sum > maximum:
            maximum = sum 
            k = i

    print("Max sum :",maximum," Range :",j,k)

# KadensAlgo([-13 ,0 ,6 ,15 ,16 ,2 ,15, -12 ,17 ,-16 ,0, -3, 19, -3, 2 ,-9, -6])
KadensAlgo([-2,-3,0,-9,4,-1,-2,1,5,-3])
        


