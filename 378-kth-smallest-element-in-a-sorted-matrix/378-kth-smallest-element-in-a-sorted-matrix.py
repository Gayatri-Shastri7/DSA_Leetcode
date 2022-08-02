class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([i for row in matrix for i in row])[k-1]    