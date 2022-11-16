# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

def sortarry(arr):
    a0 = 0
    a1 = 0
    a2 = 0
    k = 0
    for i in range(0,len(arr)):
        if  arr[i] == 0:
            a0 += 1
        elif  arr[i] == 1:
            a1 += 1
        elif arr[i] == 2:
            a2 += 1

    for j in range(0,a0):
        arr[k] = 0
        k +=1
    for j in range(0,a1):
        arr[k] = 1
        k +=1
    for j in range(0,a2):
        arr[k] = 2
        k +=1

    print("sorted array is   :", arr)


arr=[0,1,2,0,0,1,1,2,1,2,2,0,1,0,0]

print("Unsorted array is :", arr)
sortarry(arr)