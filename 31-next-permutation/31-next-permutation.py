class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        found = False
        i = len(nums)-2
        while i >=0:
            if nums[i] < nums[i+1]:           #To find the breakpoint
                found =True
                break
            i-=1
        if not found:                             #If no breakpoint then sort the list
            nums.sort()
            return nums
        else:
            j=i+1
            while j<n and nums[j]>nums[i]:
                j+=1
            j-=1

            #Swap
            nums[i],nums[j]=nums[j],nums[i]

            #rightmost change
            nums[i+1:] = nums[i+1:][::-1]
            return nums