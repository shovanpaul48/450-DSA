# Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, str: str) -> str:
        res=""
        resLen=0
        for i in range(len(str)):
            #for odd len
            l,r = i,i
            # print(i)
            while l>=0 and r<len(str) and str[l] == str[r]:
                # print("1L R",l,r)
                if (r - l +1) > resLen:
                    res = str[l:r+1]
                    resLen = r - l +1
                # print("2L R",l,r)
                l -= 1
                r += 1
                # print("3L R",l,r)
            # for even len ]
            l,r = i,i+1
            while l>=0 and r <len(str) and str[l] == str[r]:
                if (r - l +1) > resLen:
                    res = str[l:r+1]
                    resLen = r - l +1
                print("r l",r,l)
                l -= 1
                r += 1

        return res
t = Solution()
print(t.longestPalindrome("babad"))
