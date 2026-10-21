class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            if not nums:
                return -1

            pivot = nums[-1]
            
            less = []
            equal = []
            greater = []
            for e in nums:
                if e < pivot:
                    less.append(e)
                elif e > pivot:
                    greater.append(e)
                else:
                    equal.append(e)

            # print(less, greater, equal, pivot, k)
            if len(greater) == k - 1:
                return pivot
            elif len(greater) > k - 1:
                return quickSelect(greater, k)
            elif len(equal) > k - 1 - len(greater):
                return pivot

            else:
                return quickSelect(less, k - (len(greater) + len(equal)))

        ret = quickSelect(nums, k)
        # print(ret)
        return ret
            

            