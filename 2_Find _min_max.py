# Find the maximum and minimum element in an array
# Linear Serch

arr = [2, 7, 9, 3, 0, 11, -32, 98, 22]
# print(len(arr))
min = arr[0]
max = arr[0]
for i in range (0,len(arr)):
    if arr[i] <= min:
        min = arr[i]
    elif arr[i] >= max:
        max = arr[i]


print("Max value is ",max," Min value is ",min)

