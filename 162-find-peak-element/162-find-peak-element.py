class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        
        left, right = 0, len(arr)-1
        while left < right:
            mid = left + (right - left) // 2
            if (arr[mid] > arr[mid+1]):
                right = mid
            else:
                left = mid + 1
        return left
    