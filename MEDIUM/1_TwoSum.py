# Two Sum : Check if a pair with given sum exists in Array
# Complexity : O(n) (Time and Space)

def TwoSum(a,k):
    map={}

    target = k
    for i in range(len(a)):
        j = target - a[i]
        l = str(j)
        m = str(a[i])
        n = str(i)
        # print(j)
        if l in map.keys():
            # return (int(map[l]),int(l))
            temp = []
            temp.append(int(map[l]))
            temp.append(i)
            return temp
        else:
            map[m] = n

print(TwoSum([2,3,1,4],4))