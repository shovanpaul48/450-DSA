# Reverse array by recursion 


def Reverse_Array(array,s, l) :
    array[s] = array[s] + array[l]
    array[l] = array[s] - array[l]
    array[s] = array[s] - array[l]
    if s<l:
        Reverse_Array(array,s+1,l-1)


array = [3, 6, 8,9,10]

Reverse_Array(array,0,len(array)-1)
print(array)





