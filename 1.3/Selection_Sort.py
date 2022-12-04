# Selection Sort        
# Complexity : O(n^2)
# 
def SelectionSort(a):

    l = len(a)
    for i in range(l):
        min = i
        # print("i:",a[i])
        for j in range(i+1,l):
            if a[j] < a[min]:
                min = j
            # print("j",a[j])
        
        a[min],a[i] = a[i],a[min]

    
    print("After selection Sort ", a)

a =[ 3,9, 2,6,5,-1]
print("Before selection Sort ",a)
SelectionSort(a)
        
