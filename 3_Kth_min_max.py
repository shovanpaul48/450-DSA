# Find the "Kth" max and min element of an array 
# Using Quick Select 

# Kth maximum
def Find_Min_Max(arr,k):
    #using python sort function
    arr.sort()
    print(arr)

    # Insertion sort
    # Bubble sort
    

    print("Kth smallest eklement ",arr[k-1],"\nKth largest element ",arr[len(arr)-k])

arr = [3,8,0,4,11,-2,6,9,12]
print(arr)
Find_Min_Max(arr,3)



