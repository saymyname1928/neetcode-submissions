class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        import copy
        def acc(num, subsets: List[List[int]]) -> List[List[int]]:
            # given a num and pre-existing subset,
            # extend the subsets

            subsets0 = copy.deepcopy(subsets)
            subsets1 = copy.deepcopy(subsets)
            new_subsets = []

            for e in subsets0:
                new_subsets.append(e + [num])
            
            return new_subsets + subsets1
        
        subsets = [[]]
        for e in nums:
            subsets = acc(e, subsets)
        return subsets
            