from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct=Counter(arr)
        st=set()
        for i in dct:
            st.add(dct[i])
        if len(dct)==len(st):
            return True
        return False