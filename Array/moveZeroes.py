class Solution:
    def moveZeroes(self, stack: List[int]) -> None:
        for num in stack:
            if num == 0:
                stack.remove(0)
                stack.append(0)
