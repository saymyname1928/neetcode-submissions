class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for e in nums:
            if counter[e] > 0:
                return True
            counter[e] += 1
        return False

        