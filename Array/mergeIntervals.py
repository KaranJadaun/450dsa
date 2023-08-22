class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for interval in intervals:
            if (not res or interval[0] > res[-1][1]):
                res.append(interval)
            elif (interval[0] <= res[-1][1]):
                res[-1][1] = max(interval[1], res[-1][1])
        return res
