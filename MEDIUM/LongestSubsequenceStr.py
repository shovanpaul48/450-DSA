# 3. Longest Substring Without Repeating Characters
# complexity time:O(n) spece : O(1)

# import math
 
def longestUniqueSubsttr(str):
    test = ""
    # Result
    maxLength = -1
     
    # Return zero if string is empty
    if (len(str) == 0):
        return 0
    elif(len(str) == 1):
        return 1
    for c in list(str):
        current = "".join(c)
        print(current,test)
        # If string already contains the character
        # Then substring after repeating character
        if (current in test):
            test = test[test.index(current) + 1:]
        test = test + "".join(c)
        maxLength = max(len(test), maxLength)
    return maxLength
 
 
# Driver Code
string = "ABDAEBFGABEF"
print("The input string is", string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character substring is", length)
 