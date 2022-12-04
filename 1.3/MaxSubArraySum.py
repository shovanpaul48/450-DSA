# Maximum subarray length of a sum  
# complexity : O(2n) - O(n)

def SubarraySum(a,s):
    l = len(a)
    start ,end , sum = 0, 0, 0
    maxlen = 1
    for i in range(l):
        sum  = sum + a[i]
        
        if sum == s :
            if  maxlen < (end - start +1) :
                maxlen  =  (end - start +1 )
            start += 1
            end += 1
        elif sum > s:
            sum = a[i]
            start +=1
            end = i -1
        elif sum < s:
            end += 1
          
    return maxlen

print(SubarraySum([7,1,6,0],7))

