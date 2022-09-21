class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sumEven = sum(n for n in nums if not n%2)
        for q,i in queries:
            if nums[i]%2 and q%2:
                sumEven += nums[i]+q
            elif not nums[i]%2 and q%2:
                sumEven -= nums[i]
            elif not nums[i]%2 and not q%2:
                sumEven += q
            res.append(sumEven)
            nums[i] += q
        return res