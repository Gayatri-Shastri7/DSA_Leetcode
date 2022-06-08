'''
Case 1: 
    If you are having palindrome remove it. ans=1
    
Case 2:
    else return 2 (remove all a's or remove all b's)

Case 3:

if len =0. return 0

'''        
        
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s)==0:
            return 0
        elif(s[::-1]==s):
            return 1
        else:
            return 2
        

        
        
        
        
        
        
        
        
        