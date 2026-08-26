from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        elems = list(counter.keys())
        occurs = list(counter.values())

        sorted_idx = sorted(range(len(occurs)), key=lambda x: -occurs[x])
        return [elems[i] for i in sorted_idx[:k]]