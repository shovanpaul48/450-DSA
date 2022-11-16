# Reverse the array

def reversearry(arr):
    start = 0
    end = len(arr) -1
    while end > start:
        arr[start], arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr
a = [1,4,18,7,0,2,5,9,10,22,6]

a2 = reversearry(a)
print("Reversed array ",a2)
