# a = [1,1,0,1,0,1,1,1,0,1,0,0,1,1,1,1]
# # a = [1,1,0,1,1,1]

# l1 = 0
# l2 = 0
# for i in range(len(a)-1):
#     if (a[i] == a[i+1]):
#         l1 +=1
#         # print("A: i",i," a[i]: ",a[i] ,l1)
    

#     else:
#         # print("B: i",i," a[i]: ",a[i] ,l1+1)
#         if l2 < l1:
#             l2 = l1
#             l1 = 0
#         else: 
#             l1 = 0


# if l1 > l2 :
#     print (l1+1)
# else:
#     print("l2",l2+1)
    








class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]):

        l1 = 0
        l2 = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                l1 += 1 
            else : 
                if l2 < l1:
                    l2 = l1
                    l1 = 0
                else: 
                    l1 = 0


        return (max(l1,l2))
    
        
s = Solution()
print(s.findMaxConsecutiveOnes([0,1]))
