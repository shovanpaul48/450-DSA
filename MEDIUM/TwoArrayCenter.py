class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        temp = []
        if l1 > l2:
            for i in range(l2-1,-1,-1):
                if  nums1[i] > nums2[i] and nums1[i-1] < nums2[i] :
                    temp.append(nums1[i])
                    temp.append(nums2[i])
                elif nums1[i] < nums2[i] and nums1[i] > nums2[i-1]:
                    temp.append(nums2[i]) 
                    temp.append(nums1[i])
                elif nums2[i] == nums1[i]:
                    temp.append(nums1[i])
                    temp.append(nums1[i])
            # for j i 

                    
        elif l1 < l2 :
            for i in range(l2-1,-1,-1):
                if nums1[i] > nums2[i] and nums1[i] != None:
                    temp.append(nums1[i])
                elif nums1[i] < nums2[i] and nums1[i] != None:
                    temp.append(nums2[i]) 
                    temp.append(nums1[i])
                elif nums1[i] == None:
                    temp.append(nums2[i])

        elif l1 == l2 :
            for i in range(l1-1,-1,-1):
                if nums1[i] > nums2[i] :
                    temp.append(nums1[i])
                    temp.append(nums2[i])
                elif nums1[i] < nums2[i] :
                    temp.append(nums2[i]) 
                    temp.append(nums1[i])
                elif nums2[i] == None:
                    temp.append(nums1[i])
        
        l3 = len(temp)
        if l3 % 2 == 0:
            m = l3 // 2
            n  = m - 1
            avg = float((temp[m] + temp[n] ) / 2)
            return float(avg)
        else:
            m = (l3 // 2) -1
            return float(temp[m])



k = Solution()
print(k.findMedianSortedArrays([1,3],[2]))