class Solution:
    def numTrees(self, n: int) -> int:
        cache = [0]*(n+1)
        cache[0] = 1
        cache[1] = 1
        for i in range(2, n+1):
            for j in range(i): #1
                cache[i] += cache[j]*cache[i -j - 1] #2
            
        return cache[-1]
        