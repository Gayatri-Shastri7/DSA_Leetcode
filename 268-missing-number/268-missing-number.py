'''
        
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i=0
        while i < n: 
            if nums[i]<n and nums[i]!=i: 
                s = nums[i]
                nums[i], nums[s] = nums[s], nums[i]
            else:
                i += 1 
        for i in range(n):
            if nums[i]!=i: 
                return i
        return n

            
        