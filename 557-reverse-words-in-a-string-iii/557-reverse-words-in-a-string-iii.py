class Solution:
    def reverseWords(self, s: str) -> str:
        e= s.split()
        out=[]
        for i in e:
            a=list(i)
            a.reverse()
            se="".join(a)
            out.append(se)
        return(" ".join(out))
        