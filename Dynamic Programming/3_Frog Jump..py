def frogJump(n, h):
    # dp = []
    # dp.insert(0,0)
    prev1 = 0
    prev2 = 0
    for i in range (1,n):
        jump2 = 2147483648
        # jump1 = dp[i -1] + abs(h[i] - h[i-1])
        jump1 = prev1 + abs(h[i] - h[i-1])
        if i > 1:
            # jump2 = dp[i -2] + abs(h[i] - h[i-1])
            jump2 = prev2 + abs(h[i] - h[i-2])
        
        # dp.insert(i,min(jump1,jump2))
        print(jump1, jump2 )
        curr_i = min(jump1,jump2)
        prev2 = prev1
        prev1 = curr_i
    # return dp[n-1]
    return prev1

# print(frogJump(4,[10,20,30,10]))
print(frogJump(3,[10,50,10]))
# print(frogJump(6,[30,10,60,10,60,50]))