class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        while (low <= high):
            mid = (low + high) >> 1
            if (mid == x // mid): 
                return mid
            if (mid > x // mid): 
                high = mid - 1
            else:
                low = mid + 1
        return high
