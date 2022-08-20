
'''
brute force approach
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def recurMe(i,j):
            if i<0 or j<0:
                return 0
            if text1[i]==text2[j]:
                return 1+recurMe(i-1,j-1)
            else:
                return max(recurMe(i-1,j),recurMe(i,j-1))
        return recurMe(len(text1)-1,len(text2)-1)

            
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def recurMe(i,j):
            if i<0 or j<0:
                return 0
            if text1[i]==text2[j]:
                return 1+recurMe(i-1,j-1)
            else:
                return max(recurMe(i-1,j),recurMe(i,j-1))
        return recurMe(len(text1)-1,len(text2)-1)
