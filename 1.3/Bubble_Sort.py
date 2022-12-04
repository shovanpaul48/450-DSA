# Bubble Sort Algorithm
# Time Complexity: O(n^2),


def BubbleSort(a):
    l = len(a)
    for i in range(l-1):
        for j in range(l-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]


        print("After bubble Sort ", a)

    a =[ 3,9, 2,6,5,-1]
    print("Before bubble Sort ",a)
    BubbleSort(a)
            
