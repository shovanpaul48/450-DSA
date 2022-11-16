# Move all the negative elements to one side of the array 

#using partioning algorithm

def partition(arr):
    pivot=0
    i =-1
    j = 0
    for j in range(0,len(arr)):
        if arr[j] < pivot:
            i +=1
            arr[i],arr[j] = arr[j], arr[i]


    print(arr)

arr = [-3,-1,6,-6,1,8,-4]
partition(arr)
        
    
