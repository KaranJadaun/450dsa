class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if (val in hashmap):
                return [i, hashmap[val]]
            hashmap[nums[i]] = i
