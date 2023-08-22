class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        reach = 0
        end = 0
        n = len(nums)
        for i in range(n - 1):
            reach = max(reach, i + nums[i])
            if (i == end):
                cnt += 1
                end = reach
        return cnt
