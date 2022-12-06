# Maximum subarray length of a sum  
# complexity : O(n^2) 

#this algo only works for positive list 
# best solution is to use KADANE's algo

def SubarraySum(nums,s):
    l = len(nums)
    start ,end , sum = 0, -1, 0
    maxlen = 1
    f = 0
    for i in range(l):
        sum  = sum + nums[i]
        if sum == s :
            print("sum", sum , i, maxlen)
            end = i
            f = 1
            if  maxlen < (end - start +1) :
                maxlen  =  (end - start +1 )

            end += 1


        elif sum > s:
            sum = nums[i]
            start = i
            end = i
            sum = nums[i]
        elif sum < s:
            end = i
        
        
    if f == 1:
        return maxlen 
    else:
        return maxlen -1



print(SubarraySum([7,1,6,0],7))
# print(SubarraySum([-7 ,-11 ,-3 ,-7 ,4, 15 ,-13 ,18, -10, -10],23))

# print(SubarraySum([-13 ,0 ,6 ,15 ,16 ,2 ,15, -12 ,17 ,-16 ,0, -3, 19, -3, 2 ,-9, -6],15))

