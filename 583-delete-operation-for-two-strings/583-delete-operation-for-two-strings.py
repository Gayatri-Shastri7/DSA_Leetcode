class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        min_distance_dp = [[i for i in range(len(word2)+1)]] + [[i] + [math.inf] * (len(word2)) for i in range(1, len(word1)+1)]

        for i in range(len(word1)):
            for j in range(len(word2)):
                min_distance_dp[i + 1][j + 1] = min_distance_dp[i][j] if word1[i] == word2[j] else min(min_distance_dp[i+1][j], min_distance_dp[i][j+1]) + 1

        return min_distance_dp[-1][-1]