class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        
        while low < high:
            mid = low + (high - low) // 2
            current = 0
            day = 1
            for w in weights:
                if current + w > mid:
                    day += 1
                    current = 0
                current += w
            
            if day >days:
                low = mid +1 
            else:
                high = mid
            
        return low
