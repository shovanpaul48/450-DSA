# Dutch National flag algorithm
# 
# Sort an array of 0s, 1s and 2s
# Problem Statement: Given an array consisting of only 0s, 1s and 2s. 
# Write a program to in-place sort the array without using inbuilt sort functions. 
# ( Expected: Single pass-O(N) and constant space)

def sort012(a):
    l = 0
    m = 0
    h = len(a) -1
    while m <= h:
        if a[m] == 0:
            a[l],a[m] = a[m],a[l]
            l+=1
            m+=1
        elif a[m] == 1:
            m+=1
        elif a[m] == 2:
            a[h],a[m] = a[m],a[h]
            h -= 1


a = [0,2,1,0,2,2,1,1,0,0,1]
print(a)
sort012(a)
print(a)

    








