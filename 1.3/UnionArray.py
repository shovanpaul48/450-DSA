a1 = [3,6,8,0,2]
a2 = [8,6,7,2,9,1]

def union(a1,a2):
    a1 = a1 + a2
    print(a1)
    l = len(a1)
    for i in range(l-1):
        for j in range(i+1,l):
            if a1[i] == a1[j]:
                a1[j] = "False"
                # a1.remove(a1[j])
                # l = - 1
                

    return a1

print(union(a1,a2))
         
