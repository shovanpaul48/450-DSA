# Find Missing numbers
# complexity : O(n)


def FindMissingNum(a,N):
    l  = len(a)
    sum = 0
    for i in range(l):
        sum = sum + a[i]
    
    ActualSum = int(N*(N+1)/2)
    x = ActualSum - sum

    return x 

print(FindMissingNum([1, 2, 4, 6, 3, 7, 8], 8))
        
