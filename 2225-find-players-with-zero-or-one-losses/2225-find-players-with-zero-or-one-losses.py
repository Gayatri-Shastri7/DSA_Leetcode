class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        lost = Counter()

        for w,l in matches:
            lost[w] += 0
            lost[l] += 1
            
        zero = [k for k,l in lost.items() if l == 0]
        ones = [k for k,l in lost.items() if l == 1]

        return [sorted(zero), sorted(ones)]