class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if (nums[i] < nums[j]):
                   dp[i] = max(dp[i], 1 + dp[j])
            res = max(res, dp[i])
        return res
