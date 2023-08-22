class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            temp = nums[i]
            left = i + 1
            right = n - 1
            while (left < right):
                s = temp + nums[left] + nums[right]
                if (s > 0):
                    right -= 1
                elif (s < 0):
                    left += 1
                else:
                    val = [temp, nums[left], nums[right]]
                    if (val not in res):
                        res.append(val)
                    left += 1
                    right -= 1
        return res
