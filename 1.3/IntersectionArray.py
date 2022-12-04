# 1. Brute Force Approach:
# complxity = O(n^2)

a1 = [3,6,8,0,2]
a2 = [8,6,7,2,9,1]


def Intersection(a1,a2):
    l1 = len(a1)
    l2 = len(a2)
    temp = []

    if l1 < l2 :
        for i in range(l2):
            for j in range(l1):
                if a2[i] == a1[j]:
                    temp.append(a2[i])
    if l1 > l2:
        for i in range(l1):
            for j in range(l2):
                if a1[i] == a2[j]:
                    temp.append(a2[j])

    return temp

print("Brute Force Approach: ", Intersection(a1,a2))



# 2. 2 Pointer approach
# complexity = O(n)


def IntersectionArray(a1,a2):




