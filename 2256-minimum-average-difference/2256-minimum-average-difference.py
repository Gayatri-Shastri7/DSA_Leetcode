class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return 0
        total = sum(nums)
        leftSum = nums[0]
        rightSum = total - leftSum
        
        minAbs = [abs(math.floor(leftSum/1) - math.floor(rightSum/(n-1))),0]
        for i in range(1,n):
            leftSum += nums[i]
            rightSum = total - leftSum
            if(leftSum == total):
                temp = math.floor(abs(leftSum/(i+1)))
            else:
                temp = abs(math.floor(leftSum/(i+1)) - math.floor(rightSum/(n-i-1)))
            print(temp)
            if(temp < minAbs[0]):
                minAbs = [temp,i]
        return minAbs[1]

            