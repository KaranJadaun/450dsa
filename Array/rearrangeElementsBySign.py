class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        p = 0
        n = 1
        for num in nums:
            if (num > 0):
                arr[p] = num
                p += 2
            else:
                arr[n] = num
                n += 2
        return arr
