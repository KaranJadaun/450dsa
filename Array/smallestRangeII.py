class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = nums[n - 1] - nums[0]
        for i in range(n - 1):
            j = i + 1
            low = min(nums[0] + k, nums[j] - k)
            high = max(nums[n - 1] - k, nums[i] + k)
            res = min(res, high - low)
        return res
