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
        if len(nums) == 1:
            if nums[0] == 1:
                return 1
            else :
                return 0
        elif len(nums) > 1 :
            for i in range(len(nums)-1):
                if nums[i] == 1:
                    print("h")
                    l1 += 1
                    if (nums[i] == nums[i+1] ):
                        l1 +=1
                    else:
                        if l2 < l1:
                            l2 = l1
                            l1 = 0
                        else: 
                            l1 = 0
                    print("a:",l1, l2)
                
                else : 
                    print("b:",l1, l2)
                    if l2 < l1:
                        l2 = l1
                        l1 = 0
                    else: 
                        l1 = 0

            if l1 > l2 :
                if l1  > 0:
                    if l1 == 1:
                        return 1
                    else :
                        return l1 -1
                else :
                    return 0
            elif l1 == l2:
                return l1
            else:
                if l2 > 0:
                    if l2 ==1:
                        return 1
                    else:
                        return l2 -1
                else :
                    return 0
        
    
        
s = Solution()
print(s.findMaxConsecutiveOnes([0,1]))
