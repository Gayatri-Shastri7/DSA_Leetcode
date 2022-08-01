'''

Rotated Binary Search 

LOGIC:
1. Find the pivot in the array. Piviot => where your next no.s are ascending.
2. Search in first half. Single BS (0,pivot)
3. else, search in 2nd half 

CASE 1: 
    pivot element = target //Ans
CASE 2: 
    target > start element // Search for search space(s,p-1)
CASE 3:
    target < start element // ie we know that all elements from s ,pivot one of the array going to bebigger than the target.
    
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1