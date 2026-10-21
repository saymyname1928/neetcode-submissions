class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for e in nums:
            heapq.heappush(heap, e)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
            