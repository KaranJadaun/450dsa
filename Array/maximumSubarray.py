class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxi = nums[0]
        for num in nums:
            curr += num
            if (curr > maxi):
                maxi = curr
            if (curr < 0):
                curr = 0
        return maxi
