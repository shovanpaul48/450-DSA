# there are two to solve this question
# 1. frequency array 
# 2. Dictionary (hashing)

import sys
from collections import defaultdict



a = [9,8,9,0,8,-1,9,8,9,9,-1,-1,-1,-1,-1,-1]
max = 0 
min = 0
def FindMinMaxFrequency(a):

    # 1. Frequency Array 
    # ===================== 
# Stores the frequency of array
    # elements
    mp = defaultdict(int)
 
    # Find the frequency and store
    # in the map
    for i in range(len(a)):
        mp[a[i]] += 1
 
    # Initialize minFreq to the maximum
    # value and minValue to the minimum
    minFreq = sys.maxsize
    maxValue = -sys.maxsize-1
 
    # Traverse the map mp
    for x in mp:
 
        num = x
        freq = mp[x]
 
        # If freq < minFreq, then update
        # minFreq to freq and maxValue
        # to the current element
        if (freq < minFreq):
            minFreq = freq
            maxValue = num
 
        # If freq is equal to the minFreq
        # and current element > maxValue
        # then update maxValue to the
        # current element
        elif (freq == minFreq
              and maxValue < num):
            maxValue = num
        
        return maxValue

    
f = FindMinMaxFrequency(a)
print(f)






