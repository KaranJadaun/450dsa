class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        while (high >= mid):
            if (nums[mid] == 0):
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            elif (nums[mid] == 1):
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums
