class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        sub_sum = 0
        sub_sum = sum(arr)
        if sub_sum % 2 != 0: return False
        s,n = (sub_sum//2) + 1,len(arr) + 1
        dp = [[False for i in range(s)] for j in range(n)]
        for i in range(n):
            for j in range(s):
                if i == 0: 
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
        for i in range(1,n):
            for j in range(1,s):		
                if j >= arr[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]