# Find the Majority Element that occurs more than N/2 times

# We can solve this problem via HashMap but its 
# complexity will be O(NlogN) space : O(N)

# This can be reduce by Moore’s Voting Algorithm


def MooresVotingAlgo(a):
    count = 0
    element = 0
    print(a)
    for num in a:
        print( num )
        if count == 0:
            print("a :")
            element = num
 
        if num == element :
            count += 1
            print("b :", count)
        else:
            count -= 1
            print("c :", count)

    return element


a = [ 3, 2, 2, 3, 2, 2, 6,2, 3 ]
print(MooresVotingAlgo(a))


