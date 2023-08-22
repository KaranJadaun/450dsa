class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0
        n = len(height)
        right = [0] * n
        right[n - 1] = height[n - 1]
        left = height[0]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        for i in range(1, n - 1):
            left = max(left, height[i])
            diff = min(left, right[i]) - height[i]
            s += diff
        return s
