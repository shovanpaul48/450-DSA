def frogJumpWithK(n, h, k ):
    dp = []
    dp.insert(0,0)

    for i in range (1,n):
        minCost = 2147483648
        for j in range(1,k+1): 
            if i-j>=0:
                jump = dp[i-j] +  abs(h[i] - h[i-j])
                minCost = min(jump,minCost)

        dp.insert(i,minCost)
    return dp[n-1]

# print(frogJumpWithK(4,[10,20,30,10]))
# print(frogJumpWithK(3,[10,50,10]))
print(frogJumpWithK(6,[30,10,60,10,60,50],4))