class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, leftMost):
            low = 0
            high = len(nums) - 1
            temp = -1
            while (low <= end):
                mid = (low + high) >> 1
                if (nums[mid] == target):
                    temp = mid
                    if (leftMost):
                        high = mid - 1
                    else:
                        low = mid + 1
                elif (nums[mid] > target):
                    high = mid - 1
                else:
                    low - mid + 1
            return temp
        left = binarySearch(nums, True)
        right = binarySearch(nums, False)
        return [left, right]
