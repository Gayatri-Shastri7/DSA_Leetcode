class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def strip(s):
            a = list(s)
            x = i = 0
            while i < len(a):
                
                if a[i] != "#":
                    a[x] = a[i]
                    x += 1
                elif x > 0:
                    x -= 1
                    
                i += 1
                
            a = a[:x]
            return "".join(a)

        s = strip(s)
        t = strip(t)
        return True if s == t else False    