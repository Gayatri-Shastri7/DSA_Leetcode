class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        lst = list(map(list, zip(*grid)))
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if(grid[i] == lst[j]):
                    ans += 1
        return ans
        