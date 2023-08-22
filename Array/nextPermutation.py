class Solution:
    def nextPermutation(self, nums: List[int]):
        def reverse(arr, start):
            end = len(arr) - 1
            while (start < end):
                arr[start], nums[end] = nums[end], arr[start]
                start += 1
                end -= 1
        i = len(nums) - 2
        while (i >= 0 and nums[i + 1] <= nums[i]):
            i -= 1
        temp = nums[i]
        if (i >= 0):
            j = len(nums) - 1
            while (temp >= nums[j]):
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        reverse(nums, i + 1)
