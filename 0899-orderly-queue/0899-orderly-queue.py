class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k>1:
            return "".join(sorted(s))
        output=s
        for i in range(len(s)):
            output=min(output,s[i:]+s[:i])
        return output 
