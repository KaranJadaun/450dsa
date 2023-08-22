class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, -1 * num)
        temp = -1
        for i in range(k):
            temp = -1 * heapq.heappop(heap)
        return temp
