# Divide Two Integers

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. 
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers within 
# the 32-bit signed integer range: [−231, 231 − 1]. For this problem, 
# if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient 
# is strictly less than -231, then return -231.

# APPROACH 1:
# -------------
# Let a/b = c.
# Take log on both sides
# log(a) – log(b) = log(c)
# Now Log of RHS can be written as exp in LHS
# Final formula is : exp(log(a) – log(b)) = c

import  math
class Solution:
    def divide(self, a: int, b: int) -> int:
        dividend = a
        divisor = b
        # 2^31 -1 = 2147483648 -1 = 2147483647
        # Calculate sign of divisor i.e., sign will be negative
        # only if either one of them is negative otherwise itwill be positive
 
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    
        # Remove signs ofdividend and divisor
        dividend = abs(dividend)
        divisor = abs(divisor)

        if (dividend == 0):
            return 0
        if (dividend >= 2147483648):
            return sign*(2147483647)
        if (divisor == 1):
            return  (sign * dividend)

    
        # Using Formula
        # derived above.
        output = sign* math.floor(math.exp(math.log(dividend) - math.log(divisor)))
        return output
k = Solution()

# print(k.divide(568729,57))

print(k.divide(7,-3))
print(k.divide(-2147483648,-1))
            






 