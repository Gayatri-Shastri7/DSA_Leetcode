class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        lst = list(palindrome)
        for i, c in enumerate(lst):
            if c != "a":
                lst[i] = "a"
                if len(set(lst)) == 1:
                    lst[-1] = "b"
                    lst[i] = c
                break
        else:
            if len(set(lst)) == 1:
                lst[-1] = "b"
        return "".join(lst)
