from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            counter = defaultdict(int)
            nums.sort()
            for e in nums:
                counter[e] = max(counter[e-1] + 1, 1)
            return max(list(counter.values()))
        return 0