# Insertion Sort Algorithm
# Time Complexity: O(n^2), (nested for loop)
    

def InsertionSort(arr):    
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


    print("After Insertion Sort ", arr)

a =[ 3,9, 2,6,5,-1]
print("Before Insertion Sort ",a)
InsertionSort(a)
        

