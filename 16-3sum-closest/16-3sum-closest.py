class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        # Let's assume the closest as :
        closest = nums[0]+nums[1]+nums[n-1]

        for i in range(n-2):
            j = i+1
            k = n-1

            while(j<k):
                cur_sum = nums[i]+nums[j]+nums[k]
                if(cur_sum<=target):
                    j = j+1
                else:
                    k = k-1
                if(abs(closest-target)>abs(cur_sum-target)):
                    closest = cur_sum

        return closest
