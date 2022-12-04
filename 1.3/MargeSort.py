#Marge Sort

# Time complexity: O(nlogn) 
# Reason: At each step, we divide the whole array, for that logn and we assume n steps are taken to get sorted array, so overall time complexity will be nlogn
# Space complexity: O(n)  
# Reason: We are using a temporary array to store elements in sorted order
# Auxiliary Space Complexity: O(n)

# def MargeSort(a,start,end):
    




# print("After Marge Sort ", a)

# a =[ 3,9, 2,6,5,-1]
# print("Before Marge Sort ",a)
# MargeSort(a)
        
a = [2, 7, 8, 3]
a.append(9)
# print(a)
lw = len(a)
print(a, lw)
def recursiveArrayStore(a,s,l):
    if l > s:
        a[s],a[l] = a[l],a[s]
        # print(a[s],a[l])
        recursiveArrayStore(a,s+1,l-1)
        
    else:
        print(a)
        
recursiveArrayStore(a,0,lw-1)
