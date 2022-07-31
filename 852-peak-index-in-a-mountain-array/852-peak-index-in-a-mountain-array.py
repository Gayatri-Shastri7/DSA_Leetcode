class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if (arr[mid]>arr[mid+1]):
                right = mid
            else:
                left = mid + 1
        return left
    
'''
2 sorted arrays

So , will use Binary Search 

Logic:
If element at middle > e[mid+1]
'''
