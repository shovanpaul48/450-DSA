
a = [ 1, 3, 3, 7, 8, 9, 1, 1, 8, 9]
# l = len(a)

# for i in range(0,l-1):
#     print(a[i])

def RemoveDuplicates(a) :
    l = len(a)
    for i in range(l-1):
        for j in range(1,l):
            if a[i] == a[j] :
                print("= ",a[i] , a[j])
                j+=1
            else:
                print("!=",a[i] , a[j])
                i+=1
                a[i] = a[j]

print(a)
RemoveDuplicates(a)
print(a)