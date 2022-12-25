# You are given an array/list of ‘N’ integers. You are supposed to return the maximum sum of the subsequence 
# with the constraint that no two elements are adjacent in the given array/list.


# addaing dp array will reduce time complexity but increase space complexity 
def f(ind,nums,dp):
    if ind == 0 :
        return nums[ind]
    elif ind < 0:
        return 0
    elif dp[ind] != -1:
        return dp[ind]
    
    pick = nums[ind] +f(ind-2,nums,dp)
    not_pick = 0 +f(ind-1,nums,dp)
    
    dp[ind] = max(pick,not_pick)
    
    return dp[ind] 

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    dp = [-1 for element in range(len(nums))]
    return f(len(nums) -1, nums, dp )



a = [9,2,0,1,6,9]
b = [2, 1, 4, 9,5,6]

# dp[]
print(maximumNonAdjacentSum(a))
print(maximumNonAdjacentSum(b))


# Use tabulation to reduce space complexity
def solve(nums):
    prev = nums[0]
    prev2 =0
    
    for i in range(1,len(nums)):
        pick = nums[i]
        if i>1 :
            pick += prev2
        nonPick = 0 + prev
        
        cur_i = max(pick, nonPick)
        prev2 = prev
        prev= cur_i
        
    return prev

print(solve(a))
print(solve(b))