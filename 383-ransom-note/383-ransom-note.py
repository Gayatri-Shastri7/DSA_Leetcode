'''

1. Looks like if substring is present in the given sting
2. LCS Variation Problem 
3. 

'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for s in ransomNote:
            if s not in magazine:
                return False
            magazine.remove(s)
        return True
