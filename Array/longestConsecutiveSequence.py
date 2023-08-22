class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums) 
        maxi = 0
        for i in nums:
            if (i - 1 not in nums): 
                num = i
                cnt = 1
                while (num + 1 in nums):
                    cnt += 1
                    num += 1
                maxi = max(maxi, cnt)
        return maxi
