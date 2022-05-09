class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        deque = collections.deque()
        res = -math.inf

        for point in points:
            x, y = point[0], point[1]
            
            while deque and x - deque[0][0] > k:
                deque.popleft()
            
            if deque:
                res = max(res, (y + deque[0][1]) + (x - deque[0][0]))
            
            # while deque AND any equation including (x, y) will always yield a greater
			# (or ==) result than any equation including (deque[-1][0], deque[-1][1])
            while deque and (deque[-1][0] - x) + (y - deque[-1][1]) >= 0:
                deque.pop()
            
            deque.append(point)
        
        return res