class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = float('-inf')
        h = []  # max heap (-(points[i][1]-points[i][0]), points[i][0])
        ans = float('-inf')
        for xj, yj in points:
            while h and abs(h[0][1]-xj)>k:
                heappop(h)
            if h:
                ans = max(ans, -h[0][0]+xj+yj)
            heappush(h, (-(yj-xj), xj))
        return ans
