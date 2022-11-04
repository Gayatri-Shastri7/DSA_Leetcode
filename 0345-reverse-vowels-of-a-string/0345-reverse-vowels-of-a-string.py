class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l = set('aeiouAEIOU')
        i, j = 0, len(s) - 1
        while i < j:
            while s[i] not in l and i < j:
                i += 1
            while s[j] not in l and i < j:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)
