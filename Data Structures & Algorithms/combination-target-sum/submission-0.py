class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def acc(start:int, target: int, history = List[int]) -> List[List[int]]:
            if target == 0:
                return [history]

            ret = []

            for i in range(start, len(nums)):
                e = nums[i]

                if e <= target:
                    ret.extend(acc(i, target - e, history + [e]))
            return ret

        tmp = acc(0, target, [])
        return tmp
