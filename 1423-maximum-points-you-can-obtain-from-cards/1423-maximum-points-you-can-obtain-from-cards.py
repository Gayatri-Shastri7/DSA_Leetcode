class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)
        left, right = k-1, size-1
        current_pick = sum(cardPoints[:k])
        max_point = current_pick        
        for _ in range(k):            
            current_pick += ( cardPoints[right] - cardPoints[left] )            
            max_point = max(max_point, current_pick)            
            left, right = left-1, right-1
        return max_point