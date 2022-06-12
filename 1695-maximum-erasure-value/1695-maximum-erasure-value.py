'''
LOGIC:

1. a=[]

2. Append everything from nums in to 'a' one by one. 

3. If its already in that list, then dont append.

4. Then sort a.

'''

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = float('-inf')
        cur = 0
        # sliding window; current value = [i, j]
        seen = set()
        i = 0
        for j in range(len(nums)):
            while nums[j] in seen:
                cur -= nums[i]
                seen.remove(nums[i])
                i += 1
            seen.add(nums[j])
            cur += nums[j]
            ans = max(ans, cur)
            
        return ans
            
            