class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        base = [[]]
        nums = sorted(nums)

        def acc(nums, cur_subset, idx):
            ret = []
            e = nums[idx]
            # with e
            for subset in cur_subset:
                ret.append(subset + [e])

            return cur_subset + ret
        
        for i in range(len(nums)):
            base = acc(nums, base, i)
        
        final_ret = []
        for e in base:
            if e not in final_ret:
                final_ret.append(e)
        return final_ret
                
            
            